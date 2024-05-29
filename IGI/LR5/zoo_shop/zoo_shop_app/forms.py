import django.forms
from django.contrib.auth import forms
from zoo_shop_app.models import *
from zoo_shop_app.models import Review
from django.core.exceptions import ValidationError
import re


class UserRegistrationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        birth_date = models.DateField(
            validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=18 * 365),
                                          message="Вы должны быть старше 18 лет для регистрации!!!")], null=True)
        user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
        name = models.CharField(max_length=30, unique=True)
        email = models.EmailField(max_length=50, unique=True)
        phone = models.CharField(max_length=13, unique=True)
        password = models.CharField(max_length=50)


def validate_phone_number(value):
    phone_pattern = re.compile(r'^\+37529\d{7}$')
    if not phone_pattern.match(value):
        raise ValidationError('Неверный формат номера телефона. Номер должен начинаться с "+37529" и иметь 13 символов.')


class ProfileRegistrationForm(django.forms.ModelForm):
    phone = django.forms.CharField(validators=[validate_phone_number])

    class Meta:
        model = Client
        fields = ('name', 'email', 'birth_date', 'phone', 'photo')
        widgets = {
            'birth_date': django.forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'photo': django.forms.FileInput(attrs={'class': 'form-control', 'required': False})
        }


class LoginForm(django.forms.Form):
    username = django.forms.CharField()
    password = django.forms.CharField(widget=django.forms.PasswordInput)


class ProfileForm(django.forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'birth_date', 'phone', 'photo')
        widgets = {'birth_date': django.forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                   'photo': django.forms.FileInput(attrs={'class': 'form-control', 'required': False})
                   }


class ReviewForm(django.forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rate']


class VacancyForm(django.forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['position', 'description', 'salary']


class PromocodeForm(django.forms.ModelForm):
    class Meta:
        model = Promocode
        fields = ['discount', 'archived', 'code', 'text', 'valid_date']
        widgets = {
            'valid_date': django.forms.DateInput(attrs={'type': 'date'}),
        }


class AddToCartForm(django.forms.Form):
    quantity = django.forms.IntegerField(min_value=1, max_value=10, initial=1)


class AddressForm(django.forms.Form):
    address = django.forms.CharField(max_length=100, required=True)


class PromoCodeForm(django.forms.Form):
    promo_code = django.forms.CharField(max_length=10, required=False)


class FAQForm(django.forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
