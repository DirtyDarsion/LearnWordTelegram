from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('products/<slug:slug>/', views.ProductsListView.as_view(), name='category_products'),
    path('care/', views.CaresListView.as_view(), name='care'),
    path('price/', views.PriceView.as_view(), name='price'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('robots.txt', views.robots, name='robots.txt'),
    path('sitemap.xml', views.sitemap, name='sitemap.xml'),
    path('covid-cert/status/c4530ceb-7a4a-475c-bab2-882ees8b50ad', views.QRCode1View.as_view(), name='qr_code1'),
    path('covid-cert/status/c4530ceb-7a4a-475c-bab2-882ees8b50ab', views.QRCode2View.as_view(), name='qr_code2'),
]
