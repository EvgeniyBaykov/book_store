import os
from celery import shared_task
from django.core.files import File
from app_profile.models import ProfileAvatar


@shared_task()
def update_avatar_task(user_id, file_path):
    """
    Функция получает или создаёт объект ProfileAvatar, удаляет старую картинку,
    если она существует, и добавляет новую из временного файла, удаляет временный файл.
    """
    profile_avatar, created = ProfileAvatar.objects.get_or_create(user=user_id)
    if profile_avatar.image:
        # Удаляем старый файл аватара, если он существует
        if os.path.isfile(profile_avatar.image.path):
            os.remove(profile_avatar.image.path)

    # Открываем временный файл и сохраняем его как новое изображение
    with open(file_path, 'rb') as f:
        profile_avatar.image.save(os.path.basename(file_path), File(f), save=True)

    # Удаляем временный файл после сохранения
    os.remove(file_path)
