from django.urls import path, re_path
from .views import *  # импорт из women всех функ представления

'''соответ адресу //127.0.0.1:8000/
т.к. указали '' в
path('', include('women.urls'))'''
urlpatterns = [
    path('', WomenHome.as_view(), name='home'),  # //127.0.0.1:8000/, home - произвольное имя гл страницы
    # связываем класс представления с адресом гл стр. с помощью as_view, вызов обязателен
    path("about/", about, name='about'),  # второй параметр это функция представления
    path("addpage/", AddPage.as_view(), name='add_page'),  # name - название маршрута
    path("contact/", contact, name='contact'),
    path("login/", login, name='login'),
    path("register/", RegisterUser.as_view(), name='register'),
    path("post/<slug:post_slug>/", ShowPost.as_view(), name='post'),
    path("category/<slug:cat_slug>", WomenCategory.as_view(), name='category'),
]

