from django.shortcuts import render, redirect, get_object_or_404
from zoo_shop_app.models import Product, ShoppingCart
from zoo_shop_app.forms import AddToCartForm
import logging

logger = logging.getLogger('db_logger')


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            logger.info("AddToCartForm is valid.")
            quantity = form.cleaned_data['quantity']
            for _ in range(quantity):
                cart_item, created = ShoppingCart.objects.get_or_create(client=request.user.client, product=product,
                                                                        quantity=quantity)
            return redirect('cart_detail')
        else:
            logger.info("AddToCartForm is not valid.")
    else:
        form = AddToCartForm(initial={'product': product})
    return render(request, 'shopping_cart/add_to_cart.html', {'form': form, 'product': product})


def cart_detail(request):
    client = request.user.client
    cart_items = ShoppingCart.objects.filter(client=client)

    cart_summary = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'total_cost': item.product.price * item.quantity
        }
        for item in cart_items
    ]
    total_cost = sum(item['total_cost'] for item in cart_summary)

    return render(request, 'shopping_cart/cart_detail.html', {'cart_summary': cart_summary, 'total_cost': total_cost})


def clear_cart(request):
    ShoppingCart.objects.filter(client=request.user.client).delete()
    return redirect('cart_detail')
