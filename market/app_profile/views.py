from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from app_profile.forms import ProfileForm
from app_profile.models import Profile, ProfileAvatar


class AccountView(TemplateView):
    """Личный кабинет"""

    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = 'account'
        context['profile'] = Profile.objects.get(user_id=self.request.user.id)
        return context


class ProfileView(View):
    """Страница профиля"""

    def get(self, request):

        if request.user.is_authenticated:
            profile = Profile.objects.get(user_id=self.request.user.id)
            profile_form = ProfileForm(instance=profile)
            return render(request, 'profile.html', context={'profile_form': profile_form,
                                                            'active_menu': 'profile',
                                                            'profile': profile})
        else:
            return HttpResponseRedirect('/login/')

    def post(self, request):
        profile = Profile.objects.get(user_id=self.request.user.id)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        # Проверить, почему форма не проходит валидацию!!!!
        if profile_form.is_valid():
            user = Profile.objects.get(user_id=self.request.user.id)
            image = profile_form.cleaned_data.pop('avatar')
            data = request.get('email')
            print('data', data)
            if image:
                ProfileAvatar.objects.filter(user_id=user).update(image=image)

            filled_fields = {key: value for key, value in profile_form.cleaned_data.items() if value}
            print(filled_fields)
            if 'first_name' in filled_fields:
                Profile.objects.filter(id=user).update(first_name=filled_fields['first_name'])
            if 'last_name' in filled_fields:
                Profile.objects.filter(id=user).update(last_name=filled_fields['last_name'])
            if 'email' in filled_fields:
                User.objects.filter(id=user).update(email=filled_fields['email'])
            if 'phone' in filled_fields:
                print(filled_fields['phone'])
                Profile.objects.filter(id=user).update(last_name=filled_fields['phone'])

            return HttpResponseRedirect('success/')

        return render(request, 'profile.html', context={'profile_form': profile_form, 'active_menu': 'profile'})
