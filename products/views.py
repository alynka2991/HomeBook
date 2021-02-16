from .models import Category, Measure
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin


class Index(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
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
