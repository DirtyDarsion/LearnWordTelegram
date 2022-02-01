from django.urls import path
from .views import IndexListView, ProductsListView, test


urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('products', ProductsListView.as_view(), name='products'),
    path('test', test, name='test')
]
