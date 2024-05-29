from django.shortcuts import render, redirect, get_object_or_404
from zoo_shop_app.models import ShoppingCart, Sales, Promocode
from zoo_shop_app.forms import AddressForm, PromoCodeForm
import logging
from decimal import Decimal

logger = logging.getLogger('db_logger')


def create_order(request):
    client = request.user.client
    cart_items = ShoppingCart.objects.filter(client=client)

    if not cart_items.exists():
        logger.info("Cart is empty!")
        return redirect('cart_detail')

    applied_promo_code = None

    if request.method == 'POST':
        form = AddressForm(request.POST)
        promo_code_form = PromoCodeForm(request.POST)

        if form.is_valid() and promo_code_form.is_valid():
            logger.info("Forms are valid.")
            address = form.cleaned_data['address']
            promo_code = promo_code_form.cleaned_data['promo_code'].strip()

            try:
                applied_promo_code = Promocode.objects.get(code=promo_code)
                if applied_promo_code.is_valid():
                    total_cost = sum(item.product.price * item.quantity for item in cart_items)
                    promo_code_discount = applied_promo_code.discount
                    discount_amount = total_cost * (promo_code_discount / Decimal(100))
                    total_cost = max(total_cost - discount_amount, 0)

                    order = Sales.objects.create(
                        client=client,
                        total_cost=total_cost,
                        address=address
                    )

                    for item in cart_items:
                        order.products.add(item.product)

                    cart_items.delete()

                    logger.info(f"Promo code '{promo_code}' applied with discount {promo_code_discount}%.")
                    return redirect('order_confirmation', order_id=order.id)
                else:
                    logger.info(f"Promo code '{promo_code}' is not valid.")
            except Promocode.DoesNotExist:
                logger.info(f"Promo code '{promo_code}' does not exist.")
        else:
            logger.info("Forms are not valid.")
    else:
        form = AddressForm()
        promo_code_form = PromoCodeForm()

    cart_summary = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'total_cost': item.product.price * item.quantity
        }
        for item in cart_items
    ]
    total_cost = sum(item['total_cost'] for item in cart_summary)

    return render(request, 'shopping_cart/enter_address.html',
                  {'form': form, 'promo_code_form': promo_code_form, 'cart_summary': cart_summary, 'total_cost': total_cost, 'applied_promo_code': applied_promo_code})


def order_confirmation(request, order_id):
    order = get_object_or_404(Sales, id=order_id, client=request.user.client)
    return render(request, 'shopping_cart/order_confirmation.html', {'order': order})
