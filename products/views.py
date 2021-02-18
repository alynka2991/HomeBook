from .models import Category, Measure, Product
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy


class Index(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.filter(product_category__isnull=True)
        return context


class CategoryListView(generic.ListView):
    model = Category


# Дополнительная информация о категории
class CategoryDetailView(generic.DetailView):
    model = Category


# изменение данных о категории в БД
class CategoryUpdate(PermissionRequiredMixin, UpdateView):
    model = Category
    fields = '__all__'
    permission_required = 'products.can_mark_returned'


class CategoryDelete(PermissionRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
    permission_required = 'products.can_mark_returned'


class CategoryCreate(PermissionRequiredMixin, CreateView):
    model = Category
    fields = ['category_name', 'category_description']
    permission_required = 'catalog.can_mark_returned'


class MeasureListView(generic.ListView):
    model = Measure


# Дополнительная информация о единице измерения
class MeasureDetailView(generic.DetailView):
    model = Measure


# изменение данных о единице измерения в БД
class MeasureUpdate(PermissionRequiredMixin, UpdateView):
    model = Measure
    fields = '__all__'
    permission_required = 'products.can_mark_returned'


class MeasureDelete(PermissionRequiredMixin, DeleteView):
    model = Measure
    success_url = reverse_lazy('measures')
    permission_required = 'products.can_mark_returned'


class MeasureCreate(PermissionRequiredMixin, CreateView):
    model = Measure
    fields = ['measure_name', 'short_measure_name']
    permission_required = 'catalog.can_mark_returned'

