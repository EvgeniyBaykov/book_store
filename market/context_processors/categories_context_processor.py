from app_market.models import Genre


def get_categories(request):
    """Функция получает все жанры из БД"""
    genres = Genre.objects.select_related('parent').all()
    return {'categories': genres}
