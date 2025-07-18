from django.http import HttpResponse
from django.shortcuts import render


from goods.models import Categories
# Создаем тут свои странички
# Create your views here.

def index(request):
    
    
    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
        'categories': Categories

    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему..."

    }
    
    return render(request, 'main/about.html', context)
    