from django.shortcuts import render
from zoo_shop_app.models import Category, Product


def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    category_id = request.GET.get('category')
    if category_id and category_id != 'all':
        products = products.filter(category_id=category_id)

    price = request.GET.get('price')
    name = request.GET.get('name')

    if price:
        try:
            price = float(price)
            products = products.filter(price=price)
        except ValueError:
            price = None  # Игнорируем фильтрацию по цене, если введено недопустимое значение

    if name:
        products = products.filter(name__icontains=name)

    sort_by = request.GET.get('sort')
    price_sort = request.GET.get('price_sort')

    if sort_by:
        if sort_by == 'name':
            products = products.order_by('name')
        elif sort_by == 'price':
            if price_sort == 'asc':
                products = products.order_by('price')
            elif price_sort == 'desc':
                products = products.order_by('-price')

    return render(request, 'products.html', {'categories': categories, 'products': products, 'sort_by': sort_by, 'price_sort': price_sort, 'price': price, 'name': name})
