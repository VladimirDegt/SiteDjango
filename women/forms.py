from django import forms
from .models import *
# from django.core.exception import ValidationError
from django.contrib.auth.forms import UserCreationForm, User
# User объект, который работает с auth_user в БД
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

class RegisterUserForm(UserCreationForm):
    """Поскольку в джанго widgets в Meta для полей кроме username не работают, то
    мы их назначим в основном классе"""
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
