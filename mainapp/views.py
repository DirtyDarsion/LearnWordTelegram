from django.shortcuts import render
from django.views import generic
from .models import Products


class IndexListView(generic.ListView):
    model = Products
    context_object_name = 'products'
    queryset = Products.objects.filter(show_in_index=True)
    template_name = 'mainapp/content.html'

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        edges = ['Бесплатная доставка при заказе от 1000 рублей',
                 'Профессиональная обработка шаров',
                 'Индивидуальные надписи',
                 'Выполняем срочные заказы',
                 'Доставка 24/7']
        context['edges'] = edges
        return context


class ProductsListView(generic.ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'mainapp/products.html'


def care(request):
    return render(request, 'mainapp/care.html')


def qr_code(request):
    return render(request, 'mainapp/qr-code.html')


def qr_code1(request):
    return render(request, 'mainapp/qr-code1.html')
