from django.shortcuts import render
from django.views import generic
from .models import Products, Category, Cares


class IndexListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    queryset = Category.objects.filter(show=True).order_by('priority')
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        edges = [
            'Бесплатно доставляем при заказе от 1500 рублей',
            'Создаем предварительный проект композиции',
            'Профессионально обрабатываем шары',
            'Делаем индивидуальные надписи и рисунки',
            'Выполняем срочные заказы',
            'Доставка 24/7',
        ]
        context['edges'] = edges
        return context


class ProductsListView(generic.ListView):
    model = Products
    paginate_by = 16
    context_object_name = 'products'
    template_name = 'mainapp/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        if 'slug' in self.kwargs:
            context['current_category'] = Category.objects.get(slug=self.kwargs['slug'])
        else:
            context['current_category'] = None
        return context

    def get_queryset(self):
        if 'slug' in self.kwargs:
            category_id = Category.objects.get(slug=self.kwargs['slug']).id
            return Products.objects.filter(category=category_id).order_by('-id')
        else:
            return Products.objects.all().order_by('-id')


class CaresListView(generic.ListView):
    model = Cares
    context_object_name = 'cares'
    template_name = 'mainapp/care.html'


class AboutView(generic.TemplateView):
    template_name = 'mainapp/about.html'


class PriceView(generic.TemplateView):
    template_name = 'mainapp/price.html'


def sitemap(request):
    return render(request, 'mainapp/sitemap.xml', content_type='text/xml')


def robots(request):
    return render(request, 'mainapp/robots.txt', content_type='text')
