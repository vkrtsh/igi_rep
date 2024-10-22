from zoo_shop_app.models import Promocode
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from zoo_shop_app.forms import PromocodeForm
import logging
from django.contrib import messages
from zoo_shop_app.views_app.shopping_cart import get_cart_summary, calculate_total_cost
from zoo_shop_app.forms import PromoCodeForm, AddressForm

logger = logging.getLogger('db_logger')


def promocode_list(request):
    promocodes = Promocode.objects.all()
    return render(request, 'promocodes/promocode_list.html', {'promocodes': promocodes})


def promocode_detail(request, promocode_id):
    promocode = get_object_or_404(Promocode, id=promocode_id)
    return render(request, 'promocodes/promocode_detail.html', {'promocode': promocode})


def promocode_create(request):
    try:
        if request.method == 'POST':
            form = PromocodeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Промокод успешно добавлен.")
                return redirect('promocode_list')
            else:
                logger.warning("Ошибка валидации формы промокода.")
                messages.error(request, "Ошибка валидации формы.")
        else:
            form = PromocodeForm()
        return render(request, 'promocodes/promocode_form.html', {'form': form})
    except Exception as e:
        logger.error(f"Произошла ошибка при создании промокода: {str(e)}")
        messages.error(request, "Произошла ошибка при создании промокода.")
        return redirect('promocode_list')


def promocode_update(request, promocode_id):
    promocode = get_object_or_404(Promocode, id=promocode_id)
    if request.method == 'POST':
        form = PromocodeForm(request.POST, instance=promocode)
        if form.is_valid():
            form.save()
            messages.success(request, "Промокод успешно обновлен.")
            return redirect('promocode_list')
        else:
            messages.error(request, "Произошла ошибка при обновлении промокода.")
    else:
        form = PromocodeForm(instance=promocode)
    return render(request, 'promocodes/promocode_form.html', {'form': form})


def promocode_delete(request, promocode_id):
    promocode = get_object_or_404(Promocode, id=promocode_id)
    if request.method == 'POST':
        promocode.delete()
        messages.success(request, "Промокод успешно удален.")
        return redirect('promocode_list')
    return render(request, 'promocodes/promocode_confirm_delete.html', {'promocode': promocode})


def promocodes(request):
    today = timezone.now().date()
    Promocode.objects.filter(valid_date__lte=today).update(archived=True)
    Promocode.objects.filter(valid_date__gt=today).update(archived=False)

    promo_active = Promocode.objects.filter(archived=False)
    promo_archived = Promocode.objects.filter(archived=True)

    return render(request, 'promocodes/promocodes.html', {
        'promo_active': promo_active,
        'promo_archived': promo_archived
    })


def checkout(request):
    applied_promo_code = None
    discount = 0

    if request.method == 'POST':
        # Создаем формы для адреса и промокода с POST-данными
        address_form = AddressForm(request.POST)
        promo_code_form = PromoCodeForm(request.POST)

        # Проверяем, корректно ли заполнены обе формы
        if address_form.is_valid() and promo_code_form.is_valid():
            # Получаем данные из формы адреса
            order_address = address_form.cleaned_data['address']

            # Проверяем, был ли введен промокод
            promo_code_input = promo_code_form.cleaned_data['promo_code']

            if promo_code_input:
                try:
                    applied_promo_code = Promocode.objects.get(code=promo_code_input, archived=False)
                    discount = applied_promo_code.discount
                    messages.success(request, f"Промокод применен: {applied_promo_code.code} со скидкой {discount}%")
                except Promocode.DoesNotExist:
                    messages.error(request, "Такого промокода не существует.")
                    # Остаемся на странице, сохраняя состояние формы
                    return render(request, 'shopping_cart/enter_address.html', {
                        'address_form': address_form,
                        'promo_code_form': promo_code_form,
                    })

            # Получаем сводку корзины и рассчитываем итоговую стоимость с учетом скидки
            cart_summary = get_cart_summary(request.user.client)
            total_cost = calculate_total_cost(cart_summary, discount)

            # Отправляем данные для отображения страницы подтверждения заказа
            return render(request, 'shopping_cart/order_confirmation.html', {
                'cart_summary': cart_summary,
                'total_cost': total_cost,
                'applied_promo_code': applied_promo_code,
            })
        else:
            # Если формы невалидны, отображаем ошибки и возвращаем форму обратно
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
            return render(request, 'shopping_cart/enter_address.html', {
                'address_form': address_form,
                'promo_code_form': promo_code_form,
            })

    # GET-запрос: отображаем пустые формы
    address_form = AddressForm()
    promo_code_form = PromoCodeForm()
    return render(request, 'shopping_cart/enter_address.html', {
        'address_form': address_form,
        'promo_code_form': promo_code_form,
    })