from django.shortcuts import render
from zoo_shop_app.models import Sales


def orders(request):
    orders = Sales.objects.all()
    return render(request, 'orders.html', {'orders': orders})
