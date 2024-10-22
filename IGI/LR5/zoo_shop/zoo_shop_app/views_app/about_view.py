from django.shortcuts import render
from zoo_shop_app.models import AboutShop


def about(request):
    shop_info = AboutShop.objects.latest('created')
    return render(request, 'about.html', {'shop_info': shop_info})
