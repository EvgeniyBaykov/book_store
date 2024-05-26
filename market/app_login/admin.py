from django.contrib import admin
from app_login.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['id', 'first_name', 'last_name', 'author', 'phone']
