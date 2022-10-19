# создание пользовательских тегов
from django import template
from women.models import *

register = template.Library()

@register.simple_tag(name='getcats')  # превращаем функцию в тег
# name='getcats' присваиваем имя тегу, если хотим
# теперь обращаться можно и getcats, и get_categories
def get_categories(filter=None):  # функция для работы простого тега
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

# тег, который будет вызывать html страницу
@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}
