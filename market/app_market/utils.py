from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator, Page
from django.db.models import Q

from app_market.models import Book
from app_settings.utils import get_setting_from_db


def make_paginator_from_list(lst, num_pages, page):
    """
    Функция получает список, разбивает на страницы и возвращает объекты с заданной страницы
    :param lst: начальный список.
    :param num_pages: Всего количество страниц.
    :param page: Номер страницы для возврата объектов.
    :return: список отзывов определенного товара заданной страницы.
    """
    paginator = Paginator(lst, num_pages)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        objects = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        objects = paginator.page(paginator.num_pages)
    return objects


def get_all_books():
    """Функция получает все книги из БД"""
    books = Book.objects.select_related('author').prefetch_related('genre').prefetch_related('tags').all()
    return books


def get_catalog_books(request):
    """
    :param request: request
    Функция возвращает:
    - список книг отфильтрованный по жанру
    - сортирует список по новизне
    """
    books = get_all_books()

    sort_by = request.GET.get('sort_by')
    genre_slug = request.GET.get('genre')
    page = request.GET.get('page')
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

    num_books_per_page = get_setting_from_db('num_books_per_page')
    books = make_paginator_from_list(books, num_books_per_page, page)
    context = {
        'cards': books,
        'add_url': add_url,
        'sort_by': sort_by
    }
    return context


def search_books_and_authors(search):
    books = get_all_books()
    books = books.filter(title__icontains=search)

    # TODO добавить поиск по авторам
    # filter(author__profile__first_name='Дем')

    context = {
        'cards': books,
    }
    return context
