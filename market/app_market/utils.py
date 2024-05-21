from app_market.models import Book


def get_all_books():
    books = Book.objects.all()
    return books
