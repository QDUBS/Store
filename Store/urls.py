from django.urls import path
from .views import Home, DeleteItem, MonthlyRecords, Search, MonthlyCalculations




urlpatterns = [
    path('home/', Home, name = 'home'),
    path('delete/<int:id>', DeleteItem, name = 'delete'),
    path('search/', Search, name = 'search'),
    path('monthly/', MonthlyRecords, name = 'monthly'),
    path('monthlycalc/', MonthlyCalculations, name = 'monthlycalc'),
]
