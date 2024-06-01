from django.contrib import admin
from app_profile.models import Profile, ProfileAvatar


class ProfileAvatarInline(admin.TabularInline):
    model = ProfileAvatar
    max_num = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['id', 'first_name', 'last_name', 'author', 'phone']
    inlines = [ProfileAvatarInline,]
