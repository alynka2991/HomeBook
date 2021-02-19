from .models import Category, Measure, Product
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .forms import ChangeProduct


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
class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')


class CategoryCreate(CreateView):
    model = Category
    fields = ['category_name', 'category_description']


class MeasureListView(generic.ListView):
    model = Measure


# Дополнительная информация о единице измерения
class MeasureDetailView(generic.DetailView):
    model = Measure


# изменение данных о единице измерения в БД
class MeasureUpdate(UpdateView):
    model = Measure
    fields = '__all__'


class MeasureDelete(DeleteView):
    model = Measure
    success_url = reverse_lazy('measures')


class MeasureCreate(CreateView):
    model = Measure
    fields = ['measure_name', 'short_measure_name']


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
'''def change_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ChangeProduct(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            product.product_value = form.cleaned_data['product_value']
            product.product_category = form.cleaned_data['product_category']
            product.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index'))

    # If this is a GET (or any other method) create the default form
    else:
        default_value = 1
        form = ChangeProduct(initial={'product_value': default_value})

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/change_product.html', context)
'''