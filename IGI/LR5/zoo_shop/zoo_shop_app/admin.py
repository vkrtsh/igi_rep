from django.contrib import admin
from zoo_shop_app.models import *


@admin.register(AboutShop)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'image')
    search_fields = ('text',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')
    ordering = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'salary', 'photo')
    search_fields = ('name', 'email', 'position')
    ordering = ('name',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'created')
    search_fields = ('question', 'answer')
    ordering = ('created',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'rate', 'created')
    search_fields = ('author__name', 'text')
    ordering = ('id',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created')
    search_fields = ('title', 'text')
    ordering = ('created',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'supplier', 'price', 'category')
    search_fields = ('article', 'name')
    ordering = ('id',)
    readonly_fields = ('article',)

    def save_model(self, request, obj, form, change):
        if not obj.article:
            existing_product = Product.objects.filter(name=obj.name).first()
            if existing_product:
                obj.article = existing_product.article
            else:
                obj.article = obj.generate_unique_article()
        super().save_model(request, obj, form, change)


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'discount', 'archived', 'code', 'valid_date')
    search_fields = ('text', 'code')
    ordering = ('id',)


@admin.register(RegularClient)
class RegularClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', )
    search_fields = ('client__name',)
    ordering = ('id',)


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_cost', 'address')
    list_filter = ('client',)
    search_fields = ('client__name', 'address')
    ordering = ('-created',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product')
    search_fields = ('client__name', 'product__name')
    ordering = ('id',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'phone', 'email')
    search_fields = ('name', 'country', 'phone', 'email')
    ordering = ('id',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'salary')
    search_fields = ('position', 'salary')
    ordering = ('salary',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')
    search_fields = ('name',)
    ordering = ('name',)



























