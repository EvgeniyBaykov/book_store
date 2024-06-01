from app_market.models import Book


def get_all_books():
    books = Book.objects.select_related('author').prefetch_related('genre').prefetch_related('tags').all()
    return books
