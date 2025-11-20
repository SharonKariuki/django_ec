from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.home, name="home"),
    path('add_category/',views.add_category, name="add_category"),
    path('category_list/',views.category_list, name="category_list"),
]
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name="home"),
    path('add_category/', views.add_category, name="add_category"),
    path('category_list/', views.category_list, name="category_list"),
    path('add_product/', views.add_product, name="add_product"),
    path('list_products/', views.list_products, name="list_products"),
]
