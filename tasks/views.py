from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from tasks.models import Task
from tasks.forms import TaskForm


class TaskList(LoginRequiredMixin, ListView):
    """
    TaskList CBV
    """

    template_name = "tasks/tasks_list.html"
    model = Task
    context_object_name = "tasks"

    def get(self, request, *args, **kwargs):
        if "list_visit_count" in self.request.session:
            self.request.session["list_visit_count"] += 1
        else:
            self.request.session["list_visit_count"] = 1
        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_visit_count'] = self.request.session.get("list_visit_count", 0)
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    """
    TaskCreate CBV
    """

    template_name = "tasks/task_create.html"
    model = Task
    context_object_name = "form"
    form_class = TaskForm
    success_url = reverse_lazy("tasks_list")

    def form_valid(self, form):
        """Override the parent method to update fields"""
        form.instance.modified_by = self.request.user
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskDetail(LoginRequiredMixin, DetailView):
    """
    TaskDetail CBV
    """

    template_name = "tasks/task_detail.html"
    model = Task


class TaskDelete(LoginRequiredMixin, DeleteView):
    """
    TaskDelete CBV
    """

    model = Task
    success_url = reverse_lazy("tasks_list")


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """
    TaskDelete CBV
    """

    model = Task
    # We have to use reverse_lazy() instead of reverse(), as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("tasks_list")
    template_name = "tasks/task_update.html"
    form_class = TaskForm
    context_object_name = "form"
