from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('zero', views.zero, name='zero'),
    path('about', views.about, name= 'about'),
    path('third', views.third, name='third'),
]
1