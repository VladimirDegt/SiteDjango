# создание класса миксинов(пер. примесей)
from women.models import *
from django.db.models import Count

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]


class DataMixin:
        paginate_by = 3  # пагинация включена в класс ListView и он передает paginator и page_obj
        # 3 кол-во элементов на одной странице
        def get_user_context(self, **kwargs):
                context = kwargs  # в этом словаре уже есть параметр title из view
                cats = Category.objects.annotate(Count('women'))  # считаем кол-во постов
                # чтобы незарегистр-е не видели определенные меню:
                user_menu = menu.copy()  # сначала делаем копию словаря menu и сохраняем в переменной
                if not self.request.user.is_authenticated:  # если в request есть объект user со св-ом автор-н
                        user_menu.pop(1)  # тогда удаляем для него {'title': "Добавить статью", 'url_name': 'add_page'}
                context['menu'] = menu
                context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0 # когда выбраны все категории, то есть подстветка
                return context