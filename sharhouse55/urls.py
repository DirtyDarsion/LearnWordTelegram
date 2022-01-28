from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls'), name='index'),
    path('admin-panel/', admin.site.urls),
]
