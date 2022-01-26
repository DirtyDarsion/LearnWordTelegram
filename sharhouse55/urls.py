from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls'), name='mainapp'),
    path('admin/', admin.site.urls),
]
