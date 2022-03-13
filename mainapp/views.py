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
            'Бесплатная доставка при заказе от 1500 рублей',
            'Профессиональная обработка шаров',
            'Выполняем срочные заказы',
            'Индивидуальные надписи',
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
        context['categories'] = Category.objects.all()
        if 'slug' in self.kwargs:
            context['title'] = Category.objects.get(slug=self.kwargs['slug']).name
        else:
            context['title'] = 'Весь каталог'
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


class PriceView(generic.TemplateView):
    template_name = 'mainapp/price.html'


class QRCode1View(generic.TemplateView):
    template_name = 'mainapp/qr-code.html'


class QRCode2View(generic.TemplateView):
    template_name = 'mainapp/qr-code1.html'
