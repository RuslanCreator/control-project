from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<category_slug>/', views.product_list,             name='product_list_by_category'), 
    path('<id>/<slug>/', views.product_detail,
    name='product_detail'),
]