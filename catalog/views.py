from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordChangeView,
)
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from django.views.generic import TemplateView, View


from catalog.forms import (
    RegistrationForm,
    UserLoginForm,
    UserPasswordResetForm,
    UserSetPasswordForm,
    UserPasswordChangeForm,
    TasksViewForm,
    TaskFilterForm,
)
from catalog.models import Programmer, Tasks, StatusOfTask


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    num_programmers = Programmer.objects.count()
    num_tasks = Tasks.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_programmers": num_programmers,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1,
    }

    return render(request, "layouts/index.html", context=context)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tasks
    template_name = "pages/task-detail.html"


class ContactUs(LoginRequiredMixin, TemplateView):
    template_name = "pages/contact-us.html"


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account created successfully!")
            return redirect("/accounts/login")
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, "accounts/sign-up.html", context)


class UserLoginView(LoginView):
    template_name = "accounts/sign-in.html"
    form_class = UserLoginForm


def logout_view(request):
    logout(request)
    return redirect("/accounts/login")


class UserPasswordResetView(LoginRequiredMixin, PasswordResetView):
    template_name = "accounts/password_reset.html"
    form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(LoginRequiredMixin, PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    form_class = UserSetPasswordForm


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/password_change.html"
    form_class = UserPasswordChangeForm


class ChangeTaskStatus(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Tasks, id=pk)
        if task.status.status == "you can take this task":
            new_status = get_object_or_404(
                StatusOfTask, status="somebody is doing this task"
            )
            task.status = new_status

        elif task.status.status == "somebody is doing this task":
            new_status = get_object_or_404(StatusOfTask, status="done")
            task.status = new_status

        current_user = request.user

        if request.user.is_authenticated:
            programmer = get_object_or_404(Programmer, pk=current_user.pk)
            task.programmer = programmer
        task.save()
        if task.status.status == "somebody is doing this task":
            return redirect("catalog:about-us")
        return redirect("catalog:my-task")


class MyTaskView(LoginRequiredMixin, generic.ListView, View):
    model = Tasks
    template_name = "pages/my-tasks.html"
    context_object_name = "my_tasks_list"
    paginate_by = 5

    def get_queryset(self):
        current_user = self.request.user
        filter_by_current_user = Tasks.objects.filter(programmer=current_user)
        return filter_by_current_user.filter(
            status__status="somebody is doing this task"
        )


class IfSuperUser(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser


class AllTasksIfAdminView(IfSuperUser, generic.ListView):
    model = Tasks
    paginate_by = 5
    template_name = "pages/tasks-if-admin.html"
    context_object_name = "tasks_list_if_admin"

    def get_context_data(self, **kwargs):
        context = super(AllTasksIfAdminView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        level = self.request.GET.get("level")
        context["level_form"] = TaskFilterForm(
            initial={"level": level},
        )
        context["search_form"] = TasksViewForm(
            initial={"name": name},
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        level = self.request.GET.get("level")
        if name:
            queryset = queryset.filter(name__icontains=name)
        if level:
            queryset = queryset.filter(level__id=level)
        return queryset


class AboutUs(LoginRequiredMixin, generic.ListView):
    model = Tasks
    template_name = "pages/about-us.html"
    context_object_name = "tasks_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        level = self.request.GET.get("level")
        context["level_form"] = TaskFilterForm(
            initial={"level": level},
        )
        context["search_form"] = TasksViewForm(
            initial={"name": name},
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status__status="you can take this task")
        name = self.request.GET.get("name")
        level = self.request.GET.get("level")
        if name:
            queryset = queryset.filter(name__icontains=name)
        if level:
            queryset = queryset.filter(level__id=level)
        return queryset


class CreateTasksView(IfSuperUser, generic.CreateView):
    model = Tasks
    success_url = reverse_lazy("catalog:tasks-if-admin")
    template_name = "pages/tasks-update.html"
    context_object_name = "task_create"
    fields = "__all__"


class DeleteTasksView(IfSuperUser, generic.DeleteView):
    model = Tasks
    success_url = reverse_lazy("catalog:tasks-if-admin")


class UpdateTasksView(IfSuperUser, generic.UpdateView):
    model = Tasks
    template_name = "pages/tasks-update.html"
    context_object_name = "task_update"
    fields = "__all__"
    success_url = reverse_lazy("catalog:tasks-if-admin")
