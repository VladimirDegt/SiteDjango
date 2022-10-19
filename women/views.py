from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
# для вывода данных из табл:
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]
def index(request):  # request это ссылка на класс HttpRequest
    posts = Women.objects.all()  # вывод из табл
    # return render(request, 'women/index.html', {'posts': posts, 'menu': menu, "title": "Главная страница"})
    """ для удобства (чтобы не скролить) все это лучше записать так:"""
    context = {  # произвольная переменная
        'posts': posts,
        'menu': menu,
        "title": "Главная страница",
        'cat_selected': 0,  # для использования в base
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, "title": "О сайте"})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception): # обработка 404 ошибки
    return HttpResponseNotFound("<h1>Упс, а нет такой страницы!</h1>")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)  # фильтруем по рубрикам (по id)

    if len(posts) == 0:  # если нет контента, то 404
        raise Http404()
    context = {
        'posts': posts,
        'menu': menu,
        "title": "Отображение по рубрикам",
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)