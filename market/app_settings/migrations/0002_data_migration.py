from django.db import migrations

from dynaconf import settings as _settings


def create_settings_data(apps, schema_editor):
    SiteSettings = apps.get_model('app_settings', 'SiteSettings')
    SiteSettings.objects.get_or_create(site_name=_settings.SITE_NAME,
                                       phone_number1=_settings.PHONE_NUMBER1,
                                       phone_number2=_settings.PHONE_NUMBER2,
                                       address=_settings.ADDRESS,
                                       banner_number=_settings.BANNER_NUMBER,
                                       stopping_sales=_settings.STOPPING_SALES,
                                       banner_cache_time=_settings.BANNER_CACHE_TIME,
                                       total_cache_time=_settings.TOTAL_CACHE_TIME,
                                       common_books_top_number=_settings.COMMON_BOOKS_TOP_NUMBER,
                                       num_reviews_per_page=_settings.NUM_REVIEWS_PER_PAGE,
                                       num_books_per_page=_settings.NUM_BOOKS_PER_PAGE
                                       )


class Migration(migrations.Migration):
    dependencies = [
        ('app_settings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_settings_data),
    ]