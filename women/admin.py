from django.contrib import admin

# чтобы стали доступны в админ панели
from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)  # поля, которые могут редактироваться в админке
    list_filter = ('is_published', 'time_create')  # поля, которые могут сортироваться в админке

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

# регистрация
admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
