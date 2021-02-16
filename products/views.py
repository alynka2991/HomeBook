from django.shortcuts import render
from .models import Product, Category, Measure
from django.views import generic


class Index(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryListView(generic.ListView):
    model = Category
