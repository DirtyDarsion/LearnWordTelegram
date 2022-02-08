from django.shortcuts import render
from django.views import generic
from .models import Products, Category, Edges, Cares


class IndexListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    queryset = Category.objects.filter(show=True).order_by('priority')
    template_name = 'mainapp/content.html'

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['edges'] = Edges.objects.all()
        return context


class ProductsListView(generic.ListView):
    model = Products
    paginate_by = 16
    context_object_name = 'products'
    template_name = 'mainapp/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if 'pk' in self.kwargs:
            context['title'] = Category.objects.get(id=self.kwargs['pk']).name
        else:
            context['title'] = 'Все работы'
        return context

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Products.objects.filter(category=self.kwargs['pk'])
        else:
            return Products.objects.all()


class CaresListView(generic.ListView):
    model = Cares
    context_object_name = 'cares'
    template_name = 'mainapp/care.html'


def price(request):
    return render(request, 'mainapp/price.html')


def qr_code(request):
    return render(request, 'mainapp/qr-code.html')


def qr_code1(request):
    return render(request, 'mainapp/qr-code1.html')
