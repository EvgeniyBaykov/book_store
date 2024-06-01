from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_login.forms import RegisterForm


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


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/registration.html', {'form': form})
