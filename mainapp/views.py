from django.shortcuts import render
from .models import Products


def index(request):
    data = {
        'Products': Products.objects.filter(show_in_index=True),
    }
    return render(request, 'mainapp/content.html', data)
