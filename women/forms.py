from django import forms
from .models import *
# from django.core.exception import ValidationError

#  форма добавления статьи
class AddPostForm(forms.ModelForm):
    # конструктор для значения по умолчанию для поля cat
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Women  # делает связь этой формы с моделью Women
        # fields = '__all__'  # говорит какие поля нужно отобразить в форме или:
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        # персональные стили для полей
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-input"}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    # создание собственного валидатора
    def clean_title(self): # clean_ + поле для которого валидация
        title = self.cleaned_data['title']
        if len(title) > 30:
            raise ValidationError('Длина превышает 200 символов')
        return title