from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView # класс для представления списков (главной страницы)
from django.views.generic import DetailView # класс для представления конкретной страницы
from django.views.generic import CreateView # класс для добавления новой статьи
from django.contrib.auth.mixins import LoginRequiredMixin  # миксин для ограничения доступа не зарегистрировваных
# пользователей к определенной странице
from django.contrib.auth.decorators import login_required  # а это запрет для функций представления как выше для классов
from django.core.paginator import Paginator
# для вывода данных из табл:
from .forms import *
from .models import *
from .utils import *



class WomenHome(DataMixin, ListView):  # класс для представления главной страницы (списка)
    model = Women  #  пытается взять все записи из таблицы Women и отобразить их вместо списка
    # т.к. по умолчанию ListView ссылается на women/women_list.html, то сделаем ссылку на готовый или создать list.html
    template_name = 'women/index.html'
    context_object_name = 'posts' # все содержание табл Women присваиваем переменной posts

    # функция для передачи значений в index.html
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # сначала берем уже существующий контекст ('posts', 'women/index.html')
        # т.к. это словарь и ему можем добавить еще элементы
        c_def = self.get_user_context(title='Главная страница')  # self.get_user_context обращение к DataMixin
        context = dict(list(context.items()) + list(c_def.items()))  # объединение двух словарей
        return context  # первый формируется на основании ListView, а второй на DataMixin

    # для выборки отображения не всех полей табл Women, а с каким то условием, создаем фук-цию:
    def get_queryset(self):
        return Women.objects.filter(is_published=True)  # только опубликованные (галочка=True)

# def index(request):  # request это ссылка на класс HttpRequest
#     posts = Women.objects.all()  # вывод из табл
#     # return render(request, 'women/index.html', {'posts': posts, 'menu': menu, "title": "Главная страница"})
#     """ для удобства (чтобы не скролить) все это лучше записать так:"""
#     context = {  # произвольная переменная
#         'posts': posts,
#         'menu': menu,
#         "title": "Главная страница",
#         'cat_selected': 0,  # для использования в base
#     }
#     return render(request, 'women/index.html', context=context)
@login_required  # запрет на доступ к странице для не зарегистрированных
def about(request):
    # пример пагинации для фук-ции представления
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'page_obj': page_obj, 'menu': menu, "title": "О сайте"})

# def addpage(request):  # фун-ция представления для формы добавления стр
#     """при первом появлении у пользователя request.method == None, а
#     при отправлении заполненной формы уже - POST"""
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():  # проверка корректности внесенных данных
#             # print(form.cleaned_data)
#             form.save()  # добавляем в БД
#             return redirect('home')  # возвращаем на главную страницу
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form,
#                                                   'menu': menu,
#                                                   "title": "Добавление статьи"})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm  # связь между классом формы и классом представления
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')  # после добавления статьи идет возврат на указанный адрес
    login_url = reverse_lazy('home')  # если пользователь не зарегистр-й, то его вернет на эту страницу
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception): # обработка 404 ошибки
    return HttpResponseNotFound("<h1>Упс, а нет такой страницы!</h1>")

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
# # фук-ция находит в Women статью с слагом, если нет то 404
#     context = {
#         'post': post,
#         'menu': menu,
#         "title": post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'women/post.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'  # для использования в urls.py значения <slug:post_slug>, т.к. по умолчанию <slug:slug>
    # pk_url_kwarg = 'pk' вариант использования айдишника, по умолчанию pk
    context_object_name = 'post' # определяем для использования в post.html
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False # если не будет первой записи, то возбуждается 404
    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория -' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat.id)
        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)  # фильтруем по рубрикам (по id)
#
#     if len(posts) == 0:  # если нет контента, то 404
#         raise Http404()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         "title": "Отображение по рубрикам",
#         'cat_selected': cat_id,
#     }
#     return render(request, 'women/index.html', context=context)
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm  # форму регистрации сделали свою в формах
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
