from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from app_login.forms import RegisterForm, UserDeleteForm


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


def register_view(request) -> any:
    """
    Функция передающая форму регистрации. Если был метод запроса POST,
    получает данные из формы, создаёт запись пользователя и авторизует его.
    """
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


class UserDeleteView(LoginRequiredMixin, View):
    """
    Удаляет текущего пользователя, вошедшего в систему, и все связанные с ним данные.
    """
    def get(self, request, *args, **kwargs):
        form = UserDeleteForm()
        return render(request, 'registration/delete_user.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            user = request.user
            logout(request)
            user.delete()
            # messages.success(request, 'Account successfully deleted')
            return HttpResponseRedirect('/')
        return render(request, 'registration/delete_user.html', {'form': form})
