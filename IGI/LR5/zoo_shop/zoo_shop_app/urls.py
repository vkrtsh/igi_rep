from django.urls import path

from zoo_shop_app.views_app.home_view import home
from zoo_shop_app.views_app.about_view import about
from zoo_shop_app.views_app.contacts_view import contacts
from zoo_shop_app.views_app.promocodes_view import *
from zoo_shop_app.views_app.privacy_policy_view import privacy_policy
from zoo_shop_app.views_app.suppliers_view import suppliers
from zoo_shop_app.views_app.account_view import register, login, logout
from zoo_shop_app.views_app.api_views import facts_about_cats, images_dogs
from zoo_shop_app.views_app.news_view import news, article_detail
from zoo_shop_app.views_app.products_view import *
from zoo_shop_app.views_app.review_view import reviews, add_review
from zoo_shop_app.views_app.vacancies_view import *
from zoo_shop_app.views_app.shopping_cart import *
from zoo_shop_app.views_app.sales_view import *
from zoo_shop_app.views_app.faq_view import *
from zoo_shop_app.views_app.orders_view import orders
from zoo_shop_app.views_app.static_view import sales_chart
from django.urls import re_path
from zoo_shop_app.views_app.download_certificate import download_certificate


urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^home/$', home, name='home'),
    re_path(r'^about/$', about, name='about'),
    re_path(r'^contacts/$', contacts, name='contacts'),
    re_path(r'^news/$', news, name='news'),
    path('article_detail/<int:id>/', article_detail, name='article_detail'),
    re_path(r'^faq/$', faq, name='faq'),
    re_path(r'^contacts/$', contacts, name='contacts'),
    re_path(r'^privacy_policy/$', privacy_policy, name='privacy_policy'),
    re_path(r'^reviews/$', reviews, name='reviews'),
    re_path(r'^add_review/$', add_review, name='add_review'),

    re_path(r'^products/$', products, name='products'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

    re_path(r'^promocodes/$', promocodes, name='promocodes'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^login/$', login, name='login'),
    re_path(r'^suppliers/$', suppliers, name='suppliers'),
    re_path(r'^logout/$', logout, name='logout'),
    re_path(r'^cats_facts/$', facts_about_cats, name='cats_facts'),
    re_path(r'^dogs_images/$', images_dogs, name='dogs_images'),

    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    re_path(r'^cart/$', cart_management, name='cart_management'),
    re_path(r'^clear-cart/$', clear_cart, name='clear_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    re_path(r'^order/create/$', create_order, name='create_order'),
    path('order/confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('update_cart/<int:item_id>/', update_cart, name='update_cart'),

    re_path(r'^orders/$', orders, name='orders'),
    re_path(r'^sales_chart/$', sales_chart, name='sales_chart'),

    re_path(r'^faq_list/$', FAQListView.as_view(), name='faq_list'),
    path('faq/<int:pk>/', FAQDetailView.as_view(), name='faq_detail'),
    re_path(r'^faq/create/$', FAQCreateView.as_view(), name='faq_create'),
    path('faq/<int:pk>/update/', FAQUpdateView.as_view(), name='faq_update'),
    path('faq/<int:pk>/delete/', FAQDeleteView.as_view(), name='faq_delete'),


    re_path(r'^vacancy_list/$', vacancy_list, name='vacancy_list'),
    re_path(r'^vacancies/create/$', vacancy_create, name='vacancy_create'),
    path('vacancies/<int:vacancy_id>/', vacancy_detail, name='vacancy_detail'),
    path('vacancies/<int:vacancy_id>/update/', vacancy_update, name='vacancy_update'),
    path('vacancies/<int:vacancy_id>/delete/', vacancy_delete, name='vacancy_delete'),


    re_path(r'^promocode_list/$', promocode_list, name='promocode_list'),
    re_path(r'^promocodes/create/$', promocode_create, name='promocode_create'),
    path('promocodes/<int:promocode_id>/', promocode_detail, name='promocode_detail'),
    path('promocodes/<int:promocode_id>/update/', promocode_update, name='promocode_update'),
    path('promocodes/<int:promocode_id>/delete/', promocode_delete, name='promocode_delete'),


    re_path(r'^download_certificate/$', download_certificate, name='download_certificate'),

]
