from django.contrib import admin
from .models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
    fields = ['name', 'show_in_index', 'category', 'text', 'price', 'img']

    list_display = ('name', 'category', 'price', 'show_in_index')
    list_filter = ['category']
    search_fields = ['name', 'text']


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category)
