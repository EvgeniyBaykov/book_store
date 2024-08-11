from app_market.models import Book, Genre


def get_all_books():
    """Функция получает все книги из БД"""
    books = Book.objects.select_related('author').prefetch_related('genre').prefetch_related('tags').all()
    return books


def get_catalog_products(request):
    """
    :param request:
    Функция возвращает:
    - список книг по поиску из любой страницы
    """
    books = get_all_books()
    context = {
        'cards': books,
    }
    return context
