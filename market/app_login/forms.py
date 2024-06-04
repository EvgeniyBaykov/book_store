from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')
        help_texts = {
            "username": ""
        }


class UserDeleteForm(forms.Form):
    """
    Форма, в которой установлен флаг, сигнализирующий об удалении аккаунта.
    """
    delete = forms.BooleanField(label='', help_text=_('Ваш аккаунт будет удален безвозвратно!'),
                                error_messages={
                                    'required': 'Пожалуйста, выберите данный пункт для удаления аккаунта'})
