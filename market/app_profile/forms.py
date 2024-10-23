from django import forms
from django.core.exceptions import ValidationError

from app_profile.models import Profile, ProfileAvatar


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False, label="Новый аватар")

    class Meta:
        model = Profile
        fields = ['phone', 'first_name', 'last_name']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Profile.objects.filter(phone=phone).exists():
            raise ValidationError('Пользователь с таким номером телефона уже существует.')
        return phone

