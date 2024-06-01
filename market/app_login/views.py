from django.shortcuts import render
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)


class LogView(LoginView):
    """
    Страница авторизации на сайте
    """
    template_name = 'login.html'


class LogoutUserView(LogoutView):
    """
    Завершение сессии пользователя
    """

    next_page = '/'


class UserResetPasswordView(PasswordResetView):
    """
    Начальный этап сброса пароля пользователя
    """

    template_name = 'registration/password_reset.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
    """
    Успешный сброс пароля пользователя
    """

    template_name = 'registration/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Ввод нового пороля и подтверждение для сброса пароля пользователя
    """

    template_name = 'registration/password_reset_confirm.html'


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    """
    Завершение сброса пароля и возможность залогиниться с новым паролем
    """

    template_name = 'registration/password_reset_complete.html'
