from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from to_do_app.forms import TaskForm, TagForm
from to_do_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "to_do_app/home.html"
    ordering = ["is_done", "-created_at"]


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_app/task_form.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = True
        return context


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_app/task_form.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = False
        return context

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("home")


class TaskToggleStatusView(generic.View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return redirect("home")

class TagListView(generic.ListView):
    model = Tag
    template_name = "to_do_app/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do_app/tag_form.html"
    success_url = reverse_lazy("tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = True
        return context

class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do_app/tag_form.html"
    success_url = reverse_lazy("tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = False
        return context

class TagDeleteView(View):
    def post(self, request, *args, **kwargs):
        tag = Tag.objects.get(pk=kwargs["pk"])
        tag.delete()
        return  redirect(reverse_lazy("tag-list"))