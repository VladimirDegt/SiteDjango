from django.urls import path, re_path
from .views import *  # импорт из women всех функ представления

'''соответ адресу //127.0.0.1:8000/
т.к. указали '' в
path('', include('women.urls'))'''
urlpatterns = [
    path('', index, name='home'),  # //127.0.0.1:8000/, home - произвольное имя гл страницы
    path("about/", about, name='about'),  # второй параметр это функция представления
    path("addpage/", addpage, name='add_page'),  # name - название маршрута
    path("contact/", contact, name='contact'),
    path("login/", login, name='login'),
    path("post/<slug:post_slug>/", show_post, name='post'),
    path("category/<int:cat_id>", show_category, name='category'),
]

