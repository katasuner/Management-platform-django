from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('main_page/', views.main_page, name='main_page'),
    path('registartion', views.RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='project/login.html', next_page='main_page'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('task_create/', views.TaskCreateView.as_view(), name='task_create'), 
    path('task_update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task_delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('all_tasks/', views.TaskListView.as_view(), name='all_tasks'),
    path('project_create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('project_update/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('project_delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('all_projects/', views.ProjectListView.as_view(), name='all_projects')


]