# Generated by Django 4.2.13 on 2024-06-04 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='имя пользователя')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='фамилия пользователя')),
                ('phone', models.BigIntegerField(blank=True, null=True, unique=True, verbose_name='номер телефона')),
                ('author', models.BooleanField(default=False, verbose_name='является ли автором')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужской'), ('W', 'Женский')], max_length=1, null=True, verbose_name='пол')),
                ('about', models.TextField(blank=True, null=True, verbose_name='о себе')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='ProfileAvatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/profiles/%Y/%m', verbose_name='аватар пользователя')),
                ('image_alt', models.CharField(default='Аватар пользователя', max_length=100, verbose_name='подсказка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_profile.profile', verbose_name='пользователь')),
            ],
        ),
    ]
