from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Project(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 3, 'Низкий'
        MEDIUM = 2, 'Средний'
        HIGH = 1, 'Высокий'

    title = models.CharField(max_length=255, verbose_name='Название проекта')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Менеджер проекта', related_name='managed_projects')
    description = models.TextField(verbose_name='Описание')
    started = models.DateField(auto_now_add=True, verbose_name='Дата начала проекта')
    updated = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    due_date = models.DateField(verbose_name='Срок завершения', null=True, blank=True)
    members = models.ManyToManyField(User, verbose_name='Участники', related_name='member_of_projects')
    status = models.CharField(max_length=50, verbose_name='Статус', choices=[('ACTIVE', 'Активный'), ('PAUSED', 'На паузе'), ('COMPLETED', 'Завершён')])

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Task(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 3, 'Низкий'
        MEDIUM = 2, 'Средний'
        HIGH = 1, 'Высокий'
    
    class Status(models.IntegerChoices):
        NOT_COMPLETED = 0, 'Выполняется'
        COMLETED = 1, 'Завершено'


    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', verbose_name='Название проекта')
    title = models.CharField(max_length=255, verbose_name='Наименование задачи')
    description = models.TextField(verbose_name='Описание')
    started = models.DateField(auto_now_add=True, verbose_name='Старт выполнения задачи')
    updated = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    due_date = models.DateField(verbose_name='Срок завершения', null=True, blank=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,  blank=True,  verbose_name='Исполнитель')
    status = models.IntegerField(choices=Status.choices, default=Status.NOT_COMPLETED, verbose_name='Статус')
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW, verbose_name='Приоритет')


class TaskComment(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='comments', verbose_name='Задача')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name = 'Комментарий к задаче'
        verbose_name_plural = 'Комментарии к задачам'

    def __str__(self):
        return f"Комментарий от {self.author} к задаче {self.task.title}"


    
