from django.contrib.auth.models import User
from django.test import Client, TestCase

from .models import SiteSettings


class TestSettingsView(TestCase):
    """Класс тестов страницы настроек сайта"""
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='admin', password='testpassword')
        self.user = User.objects.create_user(username='user', password='testpassword')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.superuser)

    def test_settings_exist(self):
        """Проверка существования записи с настройками"""
        settings = SiteSettings.objects.exists()
        self.assertTrue(settings)
