from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    index,
    AboutUs,
    ContactUs,
    Author,
    UserLoginView,
    register,
    logout_view,
    UserPasswordChangeView,
    UserPasswordResetView,
    UserPasswordResetConfirmView,
    presentation,
    page_header,
    features,
    navbars,
    nav_tabs,
    pagination,
    inputs,
    forms,
    alerts,
    modals,
    typography,
    toggles,
    progress_bars,
    dropdowns,
    buttons,
    breadcrumbs,
    badges,
    avatars,
    tooltips,
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
    path("author/", Author.as_view(), name="author"),
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
    path("presentation/", presentation, name="presentation"),
    path("page-header/", page_header, name="page_header"),
    path("features/", features, name="features"),
    path("navbars/", navbars, name="navbars"),
    path("nav-tabs/", nav_tabs, name="nav_tabs"),
    path("pagination/", pagination, name="pagination"),
    path("inputs/", inputs, name="inputs"),
    path("forms/", forms, name="forms"),
    path("alerts/", alerts, name="alerts"),
    path("modals/", modals, name="modals"),
    path("tooltips/", tooltips, name="tooltips"),
    path("avatars/", avatars, name="avatars"),
    path("badges/", badges, name="badges"),
    path("breadcrumbs/", breadcrumbs, name="breadcrumbs"),
    path("buttons/", buttons, name="buttons"),
    path("dropdowns/", dropdowns, name="dropdowns"),
    path("progress-bars/", progress_bars, name="progress_bars"),
    path("toggles/", toggles, name="toggles"),
    path("typography/", typography, name="typography"),
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
