from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('index.html', views.product_list, name='product_list'),
    path('smartphones.html', views.smartphones_list, name='smartphones_list'),
    path('<slug:category_slug>', views.product_list,
         name='product_list_by_category'),
    path('catalog/<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]