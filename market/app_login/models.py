from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """Модель описывает профиль пользователя"""
    GENDER_CHOICES = [
        ('M', _('Мужской')),
        ('W', _('Женский')),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name=_('пользователь'))
    first_name = models.CharField(max_length=200, verbose_name=_('имя пользователя'))
    last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('фамилия пользователя'))
    phone = models.BigIntegerField(unique=True, null=True, blank=True, verbose_name=_('номер телефона'))
    author = models.BooleanField(default=False, verbose_name=_('является ли автором'))
    birthday = models.DateField(blank=True, null=True, verbose_name=_('дата рождения'))
    gender = models.CharField(blank=True, null=True, max_length=1, choices=GENDER_CHOICES, verbose_name=_('пол'))
    about = models.TextField(blank=True, null=True, verbose_name=_('о себе'))

    class Meta:
        verbose_name_plural = _('Профили')
        verbose_name = _('Профиль')


class ProfileAvatar(models.Model):
    """Модель описывающая аватар пользователя"""
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name=_('пользователь'))
    image = models.ImageField(upload_to='images/profiles/%Y/%m', verbose_name=_('аватар пользователя'))
    image_alt = models.CharField(max_length=100, default=_('Аватар пользователя'), verbose_name=_('подсказка'))
