from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
# для вывода данных из табл:
from .forms import *
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

def addpage(request):  # фун-ция представления для формы добавления стр
    """при первом появлении у пользователя request.method == None, а
    при отправлении заполненной формы уже - POST"""
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():  # проверка корректности внесенных данных
            # print(form.cleaned_data)
            try:
                Women.object.create(**form.cleaned_data)  # добавляем в БД
                return redirect('home')  # возвращаем на главную страницу
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form,
                                                  'menu': menu,
                                                  "title": "Добавление статьи"})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception): # обработка 404 ошибки
    return HttpResponseNotFound("<h1>Упс, а нет такой страницы!</h1>")

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
# фук-ция находит в Women статью с слагом, если нет то 404
    context = {
        'post': post,
        'menu': menu,
        "title": post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)

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