from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, View
from app_profile.forms import ProfileForm, ProfileAvatarForm
from app_profile.models import Profile, ProfileAvatar
from app_profile.tasks import update_avatar_task
import tempfile


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
            user = User.objects.get(id=self.request.user.id)
            profile_form = ProfileForm()
            avatar = ProfileAvatar.objects.filter(user=user.profile).first
            context = {'profile_form': profile_form,
                       'active_menu': 'profile',
                       'user': user,
                       'avatar': avatar}
            return render(request, 'profile.html', context=context)
        else:
            return HttpResponseRedirect('/login/')

    def post(self, request):
        user = User.objects.get(id=self.request.user.id)
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            image = request.FILES.get('image')
            if image:
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                for chunk in image.chunks():
                    temp_file.write(chunk)
                temp_file.close()
                update_avatar_task.delay(user.profile.id, temp_file.name)

            filled_fields = {key: value for key, value in profile_form.cleaned_data.items() if value}

            if 'first_name' in filled_fields:
                Profile.objects.filter(id=user.profile.id).update(first_name=filled_fields['first_name'])
            if 'last_name' in filled_fields:
                Profile.objects.filter(id=user.profile.id).update(last_name=filled_fields['last_name'])
            if 'email' in filled_fields:
                User.objects.filter(id=user.id).update(email=filled_fields['email'])
            if 'phone' in filled_fields:
                Profile.objects.filter(id=user.profile.id).update(phone=filled_fields['phone'])
            avatar = ProfileAvatar.objects.get(user=user.profile)
            context = {'profile_form': ProfileForm(),
                       'active_menu': 'profile',
                       'user': user,
                       'avatar': avatar,
                       'result': 'success'}
            return render(request, 'profile.html', context=context)

        else:
            result = 'unsuccess'
            avatar = ProfileAvatar.objects.get(user=user.profile)
            context = {'profile_form': profile_form,
                       'active_menu': 'profile',
                       'user': user,
                       'avatar': avatar,
                       'result': result}
            return render(request, 'profile.html', context=context)