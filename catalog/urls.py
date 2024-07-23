from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    index,
    AboutUs,
    ContactUs,
    UserLoginView,
    register,
    logout_view,
    UserPasswordChangeView,
    UserPasswordResetView,
    UserPasswordResetConfirmView,
    TaskDetailView,
    ChangeTaskStatus,
    MyTaskView,
    AllTasksIfAdminView,
    UpdateTasksView,
    DeleteTasksView,
    CreateTasksView,
)


app_name = "catalog"


urlpatterns = [
    path("", index, name="index"),
    path("about-us/", AboutUs.as_view(), name="about-us"),
    path("contact-us/", ContactUs.as_view(), name="contact-us"),
    path("accounts/login/", UserLoginView.as_view(), name="login"),
    path("accounts/register/", register, name="register"),
    path("accounts/logout/", logout_view, name="logout"),
    path(
        "accounts/password-change/",
        UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password-change-done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "accounts/password-reset/",
        UserPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "accounts/password-reset-confirm/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # Sections
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path(
        "change-task-status/<int:pk>/",
        ChangeTaskStatus.as_view(),
        name="change_task_status",
    ),
    path("my-tasks/", MyTaskView.as_view(), name="my-task"),
    path("tasks-if-admin/", AllTasksIfAdminView.as_view(), name="tasks-if-admin"),
    path("update-task/<int:pk>/", UpdateTasksView.as_view(), name="update-task"),
    path("delete-task/<int:pk>/", DeleteTasksView.as_view(), name="delete-task"),
    path("create-task/", CreateTasksView.as_view(), name="create-task"),
]
