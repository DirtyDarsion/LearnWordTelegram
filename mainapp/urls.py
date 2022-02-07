from django.urls import path
from .views import IndexListView, ProductsListView, CaresListView, qr_code, qr_code1


urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('products', ProductsListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductsListView.as_view(), name='category_products'),
    path('care', CaresListView.as_view(), name='care'),
    path('covid-cert/status/c4530ceb-7a4a-475c-bab2-882ees8b50ad', qr_code, name='qr_code'),
    path('covid-cert/status/c4530ceb-7a4a-475c-bab2-882ees8b50ab', qr_code1, name='qr_code'),
]
