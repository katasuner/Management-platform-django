from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView, View
from .models import Task, Project, TaskComment
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm, UserRegisterForm, ProjectForm
from .mixins import AdminRequiredMixin, ManagerRequiredMixin



def main_page(request):
    return render(request, 'project/main_page.html')

class RegisterView(FormView):
    template_name = 'project/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        projects = Project.objects.filter(members=request.user)
        tasks = Task.objects.filter(assignee=request.user)
        return render(request, 'users/profile.html', {'projects': projects, 'tasks': tasks})
    
    

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'


class ProjectCreateView(LoginRequiredMixin, ManagerRequiredMixin,  CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create_project.html'
    context_object_name = 'projects'


class ProjectUpdateView(LoginRequiredMixin, ManagerRequiredMixin,  UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_create.html'
    success_url = reverse_lazy('main_page')


class ProjectDeleteView(LoginRequiredMixin, ManagerRequiredMixin,  UpdateView):
    model = Project
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('main_page')


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'project/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'id')
        order = self.request.GET.get('order', 'asc')
        if order == 'desc':
            sort = f'-{sort}'
        return queryset.filter(user=self.request.user).order_by(sort)



class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'project/task_create.html'
    success_url = reverse_lazy('tasks_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['is_update'] = False  
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'project/task_delete.html'
    success_url = reverse_lazy('tasks_list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'project/task_update.html'
    success_url = reverse_lazy('tasks_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['is_update'] = True  
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            'title': self.object.title,
            'description': self.object.description,
            'due_date': self.object.due_date,
            'status': self.object.status,
            'priority': self.object.priority,
        })
        return initial

    def form_valid(self, form):
        return super().form_valid(form)