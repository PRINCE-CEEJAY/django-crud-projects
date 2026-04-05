from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='get_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('create/', views.create_product, name='create_product'),
]