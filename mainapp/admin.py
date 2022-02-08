from django.contrib import admin
from .models import Products, Category, Price, Edges, Cares


class ProductsAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'img']

    list_display = ('name', 'category')
    list_filter = ['category']
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'show', 'priority', 'img']

    list_display = ['name', 'priority', 'show']
    ordering = ['-show', 'priority']
    search_fields = ['name']


class PriceAdmin(admin.ModelAdmin):
    fields = ['name', 'price']

    list_display = ['name', 'price']


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Edges)
admin.site.register(Cares)
