from django.shortcuts import render, redirect, get_object_or_404
from zoo_shop_app.models import Vacancy
from zoo_shop_app.forms import VacancyForm
import logging

logger = logging.getLogger('db_logger')


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies/vacancy_list.html', {'vacancies': vacancies})


def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return render(request, 'vacancies/vacancy_detail.html', {'vacancy': vacancy})


def vacancy_create(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            logger.info("VacancyForm is valid.")
            form.save()
            logger.info("Vacancy has been successful created.")
            return redirect('vacancy_list')
        else:
            logger.info("VacancyForm is not valid.")
    else:
        form = VacancyForm()
    return render(request, 'vacancies/vacancy_form.html', {'form': form})


def vacancy_update(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            logger.info("VacancyForm is valid.")
            form.save()
            logger.info("Vacancy has been successful updated.")
            return redirect('vacancy_list')
        else:
            logger.info("VacancyForm is not valid.")
    else:
        form = VacancyForm(instance=vacancy)
    return render(request, 'vacancies/vacancy_form.html', {'form': form})


def vacancy_delete(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.method == 'POST':
        vacancy.delete()
        logger.info("Vacancy has been successful deleted.")
        return redirect('vacancy_list')
    return render(request, 'vacancies/vacancy_confirm_delete.html', {'vacancy': vacancy})
