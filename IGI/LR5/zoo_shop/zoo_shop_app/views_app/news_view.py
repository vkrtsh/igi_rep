from django.shortcuts import render, get_object_or_404
from zoo_shop_app.models import News


def news(request):
    articles = News.objects.all()
    return render(request, 'news.html', {'articles': articles})


def article_detail(request, id):
    article = get_object_or_404(News, id=id)
    return render(request, 'article_detail.html', {'article': article})
