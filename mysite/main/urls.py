from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate_love/', views.calculate_love, name='calculate_love'),
]
