from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import random


class Base(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(default=timezone.now)
    update = lastUpdate = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class AboutShop(Base):
    text = models.TextField('Shop description')
    image = models.ImageField(upload_to='static/main/')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'about_shop'


class Category(Base):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'categories'
        ordering = ['name']


class Client(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, unique=True)
    birth_date = models.DateField(
        validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=18 * 365),
                                      message="You must be at least 18 years old to register")], null=True)
    photo = models.ImageField(upload_to='static/clients/', default='static/main/user.png')
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=50, default="")

    def __str__(self):
        return f'{self.name} {self.email} {self.phone}'

    class Meta:
        ordering = ['name']
        db_table = 'clients'


class Employee(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, unique=True)
    birth_date = models.DateField(
        validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=18 * 365),
                                      message="You must be at least 18 years old to register")], null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='static/employees/', default='static/main/user.png')
    password = models.CharField(max_length=50, default="")

    def __str__(self):
        return (f'{self.id} {self.name} {self.email} {self.phone} '
                f'{self.position} {self.salary}')

    class Meta:
        ordering = ['name']
        db_table = 'employees'


class Supplier(Base):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name} {self.country} {self.phone} {self.email}'

    class Meta:
        db_table = 'suppliers'
        ordering = ['name']


class Product(Base):
    article = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/products/', default='static/main/empty.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article} {self.name} {self.supplier} {self.price} {self.category}'

    class Meta:
        db_table = 'products'

    def save(self, *args, **kwargs):
        if not self.article:
            existing_product = Product.objects.filter(name=self.name).first()
            if existing_product:
                self.article = existing_product.article
            else:
                self.article = self.generate_unique_article()
        super(Product, self).save(*args, **kwargs)

    def generate_unique_article(self):
        while True:
            article = ''.join(random.choices('0123456789', k=6))
            if not Product.objects.filter(article=article).exists():
                return article


class FAQ(Base):
    question = models.CharField(max_length=100, default='')
    answer = models.TextField(max_length=500, default='')

    def __str__(self):
        return f'{self.id} {self.question} {self.answer}'

    class Meta:
        ordering = ['created']
        db_table = 'questions'


class News(Base):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='static/news/', default='static/main/news.png')

    def __str__(self):
        return f'{self.id} {self.title} {self.text} {self.image}'

    class Meta:
        db_table = 'news'
        ordering = ['created']


class Promocode(Base):
    discount = models.IntegerField(default=0, help_text='Discount',
                                   validators=[MinValueValidator(1), MaxValueValidator(100)])
    archived = models.BooleanField()
    code = models.CharField(max_length=10, default='zoobazar', help_text='Promocode')
    text = models.CharField(max_length=100)
    valid_date = models.DateField()

    def __str__(self):
        return f'{self.id} {self.text} {self.discount}'

    class Meta:
        db_table = 'promocodes'

    def is_valid(self):
        return not self.archived and self.valid_date >= timezone.now().date()

    def apply_discount(self, original_price):
        if self.is_valid():
            discount_amount = original_price * (self.discount / 100)
            return max(original_price - discount_amount, 0)
        return original_price


class RegularClient(Base):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.client}'

    class Meta:
        db_table = 'regular_clients'


class Review(Base):
    author = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.id} {self.author} {self.rate} {self.created}'

    class Meta:
        ordering = ['id']
        db_table = 'reviews'


class Sales(Base):
    products = models.ManyToManyField(Product)
    total_cost = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(default='Minsk, Gikalo 9', max_length=100)

    class Meta:
        ordering = ['created']
        db_table = 'sales'


class ShoppingCart(Base):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id} {self.client} {self.product}'

    class Meta:
        ordering = ['id']
        db_table = 'shopping_carts'


class Vacancy(Base):
    position = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.id} {self.salary} {self.position}'

    class Meta:
        ordering = ['salary']
        db_table = 'vacancies'


class Partner(Base):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='static/partners/')
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'partners'
        ordering = ['name']

