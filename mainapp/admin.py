from django.contrib import admin
from .models import Products, Category, Edges, Cares


class ProductsAdmin(admin.ModelAdmin):
    fields = ['name', 'show_in_index', 'category', 'img']

    list_display = ('name', 'category', 'show_in_index')
    list_filter = ['category']
    search_fields = ['name']


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category)
admin.site.register(Edges)
admin.site.register(Cares)
