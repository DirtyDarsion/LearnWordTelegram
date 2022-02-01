from django.shortcuts import render
from django.views import generic
from .models import Products


class IndexListView(generic.ListView):
    model = Products
    context_object_name = 'products'
    queryset = Products.objects.filter(show_in_index=True)
    template_name = 'mainapp/content.html'


class ProductsListView(generic.ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'mainapp/products.html'


def test(request):
    return render(request, 'mainapp/test.html')
