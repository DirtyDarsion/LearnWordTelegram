from django.shortcuts import render


def index(request):
    data = {
        'title': 'Name of page'
    }
    return render(request, 'mainapp/content.html', data)
