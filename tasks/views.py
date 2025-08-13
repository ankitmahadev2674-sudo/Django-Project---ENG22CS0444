from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import TaskForm
from .models import Task

@login_required
def dashboard(request):
    status = request.GET.get("status", "all")
    tasks = Task.objects.filter(owner=request.user)
    if status == "open":
        tasks = tasks.filter(completed=False)
    elif status == "done":
        tasks = tasks.filter(completed=True)
    counts = {
        "all": Task.objects.filter(owner=request.user).count(),
        "open": Task.objects.filter(owner=request.user, completed=False).count(),
        "done": Task.objects.filter(owner=request.user, completed=True).count(),
    }
    return render(request, "tasks/dashboard.html", {"tasks": tasks, "status": status, "counts": counts})

class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:dashboard")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Task created.")
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:dashboard")

    def form_valid(self, form):
        messages.success(self.request, "Task updated.")
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:dashboard")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Task deleted.")
        return super().delete(request, *args, **kwargs)

@login_required
def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.completed = not task.completed
    task.save(update_fields=["completed", "updated_at"])
    messages.success(request, "Task marked as completed." if task.completed else "Task marked as incomplete.")
    return redirect("tasks:dashboard")
