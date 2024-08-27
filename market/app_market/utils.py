from app_market.models import Book, Genre


def get_all_books():
    """Функция получает все книги из БД"""
    books = Book.objects.select_related('author').prefetch_related('genre').prefetch_related('tags').all()
    return books


def get_catalog_products(request):
    """
    :param request: request
    Функция возвращает:
    - список книг отфильтрованный по жанру
    - сортирует список по новизне
    """
    books = get_all_books()

    sort_by = request.GET.get('sort_by')
    genre_slug = request.GET.get('genre')
    add_url = ''

    if genre_slug:
        books = books.filter(genre__slug=genre_slug)
        add_url = f'genre={genre_slug}'

    if request.GET.get('sort_by') == 'year':
        books = books.order_by('create_date')
    elif request.GET.get('sort_by') == '-year':
        books = books.order_by('-create_date')

    # TODO добавить сортировку по популярности
    # TODO решить что делать с фильтрами (нужны ли и какие)

    context = {
        'cards': books,
        'add_url': add_url,
        'sort_by': sort_by
    }
    return context
