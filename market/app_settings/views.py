from django.core.cache import cache
from django.http import HttpResponseRedirect


def settings_post(request):
    """
    Функция обрабатывающая POST запрос со страницы настроек, ловит нажатие одной из кнопок сброса кэша.
    """
    if request.method == 'POST':
        all_cache = request.POST.get('all')
        banners = request.POST.get('banners')

        if all_cache:
            # Сброс всего кэша
            cache.clear()

        # Сброс кэша определенного раздела
        if banners:
            cache.delete('banners')

    return HttpResponseRedirect('/admin/app_settings/sitesettings/1/change/')
