from django.forms import ModelForm
from django import forms
from .models import Task, Project, TaskComment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProjectForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Участники'
    )

    class Meta:
        model = Project
        fields = ['title', 'manager', 'description', 'due_date', 'status', 'priority', 'members']
        labels = {
            'title': 'Название проекта',
            'description': 'Подробное описание',
            'due_date': 'Дата выполнения',
            'status': 'Текущий статус',
            'priority': 'Приоритет проекта'
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority']
        labels = {
            'title': 'Название задачи',
            'description': 'Подробное описание',
            'due_date': 'Дата выполнения',
            'status': 'Текущий статус',
            'priority': 'Приоритет задачи'
            'manager'
        }
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)
        super().__init__(*args, **kwargs)
        if is_update:
            for field in self.fields.values():
                field.required = False


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'placeholder': 'Введите электронную почту'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    password1 = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Логин',
            'email': 'Электронная почта',
            'password1': 'Придумайте пароль',
            'password2': 'Подтвердите пароль'
        }