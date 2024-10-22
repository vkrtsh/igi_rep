from zoo_shop_app.models import FAQ
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from zoo_shop_app.forms import FAQForm


class FAQListView(ListView):
    model = FAQ
    template_name = 'faq/faq_list.html'
    context_object_name = 'faqs'


class FAQDetailView(DetailView):
    model = FAQ
    template_name = 'faq/faq_detail.html'
    context_object_name = 'faq'


class FAQCreateView(CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'faq/faq_form.html'
    success_url = reverse_lazy('faq_list')


class FAQUpdateView(UpdateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'faq/faq_form.html'
    success_url = reverse_lazy('faq_list')


class FAQDeleteView(DeleteView):
    model = FAQ
    template_name = 'faq/faq_confirm_delete.html'
    success_url = reverse_lazy('faq_list')


def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})
