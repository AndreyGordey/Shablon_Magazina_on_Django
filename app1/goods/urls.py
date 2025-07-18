# это созданный мной urls.py для моих нужд

from django.contrib import admin
from django.urls import path

from goods import views
# прописываем тут путь к страничкам

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]

