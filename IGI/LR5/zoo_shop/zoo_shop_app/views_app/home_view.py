from django.shortcuts import render
from zoo_shop_app.models import News, Partner


def home(request):
    latest_article = News.objects.latest('created')
    partners = Partner.objects.all()
    return render(request, 'home.html', {'latest_article': latest_article, 'partners': partners})
