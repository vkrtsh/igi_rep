from django.shortcuts import render
from zoo_shop_app.models import Supplier


def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers.html', {'suppliers': suppliers})
