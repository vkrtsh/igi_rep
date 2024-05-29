from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from zoo_shop_app.forms import ReviewForm
from zoo_shop_app.models import Review
import logging

logger = logging.getLogger('db_logger')


def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            logger.info("ReviewForm is valid.")
            review = form.save(commit=False)
            review.author = request.user.client
            review.save()
            logger.info("Review has been successful added.")
            return HttpResponseRedirect(reverse('reviews'))
        else:
            logger.info("ReviewForm is not valid.")
            return render(request, "add_review.html", {"form": form})
    else:
        form = ReviewForm()
        return render(request, "add_review.html", {"form": form})


def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})
