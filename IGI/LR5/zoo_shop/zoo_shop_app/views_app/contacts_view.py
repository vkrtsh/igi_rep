from django.shortcuts import render
from zoo_shop_app.models import Employee


def contacts(request):
    employees = Employee.objects.all()
    return render(request, 'contacts.html', {'employees': employees})
