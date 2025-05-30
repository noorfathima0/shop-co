from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),  # Add this
]
