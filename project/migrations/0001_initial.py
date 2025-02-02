# Generated by Django 4.2 on 2024-07-10 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('started', models.DateField(auto_now_add=True, verbose_name='Дата начала проекта')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='Срок завершения')),
                ('status', models.CharField(choices=[('ACTIVE', 'Активный'), ('PAUSED', 'На паузе'), ('COMPLETED', 'Завершён')], max_length=50, verbose_name='Статус')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managed_projects', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер проекта')),
                ('members', models.ManyToManyField(related_name='member_of_projects', to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование задачи')),
                ('description', models.TextField(verbose_name='Описание')),
                ('started', models.DateField(auto_now_add=True, verbose_name='Старт выполнения задачи')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='Срок завершения')),
                ('status', models.IntegerField(choices=[(0, 'Выполняется'), (1, 'Завершено')], default=0, verbose_name='Статус')),
                ('priority', models.IntegerField(choices=[(3, 'Низкий'), (2, 'Средний'), (1, 'Высокий')], default=3, verbose_name='Приоритет')),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='project.project', verbose_name='Название проекта')),
            ],
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='project.task', verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'Комментарий к задаче',
                'verbose_name_plural': 'Комментарии к задачам',
            },
        ),
    ]
