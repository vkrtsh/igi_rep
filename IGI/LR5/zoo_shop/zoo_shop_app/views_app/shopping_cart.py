from django.shortcuts import render, redirect, get_object_or_404
from zoo_shop_app.models import Product, ShoppingCart
from zoo_shop_app.forms import AddToCartForm
import logging
from django.contrib import messages

logger = logging.getLogger('db_logger')


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            logger.info("AddToCartForm is valid.")
            quantity = form.cleaned_data['quantity']
            # Получаем или создаем товар в корзине
            cart_item, created = ShoppingCart.objects.get_or_create(client=request.user.client, product=product)
            # Обновляем количество товара в корзине
            cart_item.quantity += quantity
            cart_item.save()
            messages.success(request, f"{product.name} добавлен в корзину.")
            return redirect('cart_management')
        else:
            logger.info("AddToCartForm is not valid.")
            messages.error(request, "Ошибка при добавлении товара в корзину.")
    else:
        form = AddToCartForm(initial={'product': product})

    return render(request, 'shopping_cart/add_to_cart.html', {'form': form, 'product': product})


def cart_management(request):
    client = request.user.client
    cart_items = ShoppingCart.objects.filter(client=client)

    cart_summary = [
        {
            'id': item.id,
            'product': item.product,
            'quantity': item.quantity,
            'total_cost': item.product.price * item.quantity
        }
        for item in cart_items
    ]

    total_cost = sum(item['total_cost'] for item in cart_summary)

    return render(request, 'shopping_cart/cart_management.html', {
        'cart_summary': cart_summary,
        'total_cost': total_cost
    })


def clear_cart(request):
    ShoppingCart.objects.filter(client=request.user.client).delete()
    messages.success(request, "Корзина очищена.")
    return redirect('cart_management')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(ShoppingCart, id=item_id, client=request.user.client)
    cart_item.delete()
    messages.success(request, f"{cart_item.product.name} удален из корзины.")
    return redirect('cart_management')


def update_cart(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(ShoppingCart, id=item_id, client=request.user.client)

        cart_item.quantity = quantity
        cart_item.save()
        logger.info(f"Updated quantity for item {cart_item.product.name} to {quantity}.")
        messages.success(request, f"Количество товара {cart_item.product.name} обновлено до {quantity}.")
        return redirect('cart_management')

    return redirect('cart_management')


def get_cart_summary(client):
    cart_items = ShoppingCart.objects.filter(client=client)

    if not cart_items.exists():
        return []

    cart_summary = []
    for item in cart_items:
        total_cost = item.product.price * item.quantity
        cart_summary.append({
            'product': item.product,
            'quantity': item.quantity,
            'total_cost': total_cost
        })

    return cart_summary


def calculate_total_cost(cart_summary, discount=0):
    total_cost = sum(item['total_cost'] for item in cart_summary)

    if discount > 0:
        total_cost = total_cost * (1 - discount / 100)

    return total_cost
