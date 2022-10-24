from django.urls import path, re_path
from .views import *  # импорт из women всех функ представления
from django.views.decorators.cache import cache_page  # для кэширования

'''соответ адресу //127.0.0.1:8000/
т.к. указали '' в
path('', include('women.urls'))'''
urlpatterns = [
    path('', WomenHome.as_view(), name='home'),  # //127.0.0.1:8000/, home - произвольное имя гл страницы
    # path('', cache_page(60)(WomenHome.as_view()), name='home'),  # вариант с кешированием страницы
    # связываем класс представления с адресом гл стр. с помощью as_view, вызов обязателен
    path("about/", about, name='about'),  # второй параметр это функция представления
    path("addpage/", AddPage.as_view(), name='add_page'),  # name - название маршрута
    path("contact/", ContactFormView.as_view(), name='contact'),
    path("login/", LoginUser.as_view(), name='login'),
    path("logout/", logout_user, name='logout'),
    path("register/", RegisterUser.as_view(), name='register'),
    path("post/<slug:post_slug>/", ShowPost.as_view(), name='post'),
    path("category/<slug:cat_slug>", WomenCategory.as_view(), name='category'),
]

