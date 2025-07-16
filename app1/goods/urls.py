# это созданный мной urls.py для моих нужд

from django.contrib import admin
from django.urls import path

from goods import views
# прописываем тут путь к страничкам

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]