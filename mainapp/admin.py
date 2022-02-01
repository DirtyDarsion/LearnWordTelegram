from django.contrib import admin
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    fields = ['name', 'show_in_index', 'text', 'price', 'img']
    list_display = ('name', 'price', 'show_in_index')


admin.site.register(Products, ProductsAdmin)
