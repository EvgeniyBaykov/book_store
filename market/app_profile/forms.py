from django import forms
from django.core.exceptions import ValidationError

from app_profile.models import Profile, ProfileAvatar


# class ProfileForm(forms.ModelForm):
#     email = forms.EmailField(required=False)
#
#     class Meta:
#         model = Profile
#         fields = ['phone', 'first_name', 'last_name']
#
#     def clean_phone(self):
#         data = self.cleaned_data['phone']
#
#         if Profile.objects.filter(phone=data).exists():
#             # self.add_error('phone', "Пользователь с таким номером телефона уже существует.")
#             raise ValidationError('Пользователь с таким номером телефона уже существует.')
#
#         return data


class ProfileAvatarForm(forms.ModelForm):
    class Meta:
        model = ProfileAvatar
        fields = ['image']

    image = forms.ImageField(required=False)


class ProfileForm(forms.Form):
    image = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)

    def clean_phone(self):
        data = self.cleaned_data['phone']

        if Profile.objects.filter(phone=data).exists():
            raise ValidationError('Пользователь с таким номером телефона уже существует.')

        return data