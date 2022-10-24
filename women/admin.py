from django.contrib import admin
from django.utils.safestring import mark_safe

# чтобы стали доступны в админ панели
from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)  # поля, которые могут редактироваться в админке
    list_filter = ('is_published', 'time_create')  # поля, которые могут сортироваться в админке
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')  # редактируемые поля в админ
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')  # не редактируемые поля в админ
    save_on_top = True  # панель Удалить, Сохранить и т.д. дублируем вверху
    def get_html_photo(self, object):  # метод, который подставляет хтмл шаблон вместо ссылок в фото
        if object.photo:  # проверка на наличие фото
            return mark_safe(f"<img src='{object.photo.url}' width=50>")  # mark_safe - фун-ция запрещающая экранировать теги
    get_html_photo.short_description = "Миниатюра"  # устанавливаем название столбца с фото
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}  # автоматом заполнять поле slug на основании поля name в админке

# регистрация
admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

# меняем надписи в админ панели
admin.site.site_title = 'Админ-панель сайта о женщинах'
admin.site.site_header = 'Админ-панель сайта о женщинах 2'
