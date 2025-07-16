# это созданный мной urls.py для моих нужд

from django.contrib import admin
from django.urls import path

from main import views
# прописываем тут путь к страничкам

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]




