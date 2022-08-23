from django.urls import path,include
from . import views
import accounts

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customers/', views.customers),
]