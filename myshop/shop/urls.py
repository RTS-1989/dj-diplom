from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('categories/<category_slug>/', views.product_categories, name='categories'),
    path('catalog/<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('review/<int:pk>', views.add_review, name='add_review'),
]
