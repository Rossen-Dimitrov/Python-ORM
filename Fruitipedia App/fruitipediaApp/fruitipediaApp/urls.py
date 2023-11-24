from django.contrib import admin
from django.urls import path, include

from fruitipediaApp.fruits import views

urlpatterns = [
    path('', views.index, name='index page'),
    path('admin/', admin.site.urls),
    path('fruits/', include('fruitipediaApp.fruits.urls')),
]
