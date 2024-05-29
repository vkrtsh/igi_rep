from django.shortcuts import render
from zoo_shop_app.models import News


def home(request):
    latest_article = News.objects.latest('created')
    return render(request, 'home.html', {'latest_article': latest_article})
