from app_settings.models import SiteSettings


def get_setting_from_db(field_name):
    """Функция получает значение заданного поля из модели настроек"""
    setting = SiteSettings.objects.first()
    field_value = getattr(setting, field_name)
    return field_value
