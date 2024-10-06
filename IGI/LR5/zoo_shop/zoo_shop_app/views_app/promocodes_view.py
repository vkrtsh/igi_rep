from zoo_shop_app.models import Promocode
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from zoo_shop_app.forms import PromocodeForm
import logging

logger = logging.getLogger('db_logger')


def promocode_list(request):
    promocodes = Promocode.objects.all()
    return render(request, 'promocodes/promocode_list.html', {'promocodes': promocodes})


def promocode_detail(request, promocode_id):
    promocode = get_object_or_404(Promocode, id=promocode_id)
    return render(request, 'promocodes/promocode_detail.html', {'promocode': promocode})


def promocode_create(request):
    if request.method == 'POST':
        form = PromocodeForm(request.POST)
        if form.is_valid():
            logger.info("PromocodeForm is valid.")
            form.save()
            logger.info("Promocode has been successful added.")
            return redirect('promocode_list')
        else:
            logger.info("PromocodeForm is not valid.")
    else:
        form = PromocodeForm()
    return render(request, 'promocodes/promocode_form.html', {'form': form})


def promocode_update(request, promocode_id):
    promocode = get_object_or_404(Promocode, id=promocode_id)
    if request.method == 'POST':
        form = PromocodeForm(request.POST, instance=promocode)
        if form.is_valid():
            logger.info("PromocodeForm is valid.")
            form.save()
            logger.info("Promocode has been successful edited.")
            return redirect('promocode_list')
        else:
            logger.info("PromocodeForm is not valid.")
    else:
        form = PromocodeForm(instance=promocode)
    return render(request, 'promocodes/promocode_form.html', {'form': form})


def promocode_delete(request, promocode_id):
    promocode = get_object_or_404(Promocode, id=promocode_id)
    if request.method == 'POST':
        promocode.delete()
        logger.info("Promocode has been successful deleted.")
        return redirect('promocode_list')
    return render(request, 'promocodes/promocode_confirm_delete.html', {'promocode': promocode})


def promocodes(request):
    Promocode.objects.filter(valid_date__lte=datetime.today()).update(archived=True)
    Promocode.objects.filter(valid_date__gt=datetime.today()).update(archived=False)
    promo_active = Promocode.objects.filter(archived=0)
    promo_archived = Promocode.objects.filter(archived=1)
    return render(request, 'promocodes/promocodes.html',
                  {'promo_active': promo_active, 'promo_archived': promo_archived})
