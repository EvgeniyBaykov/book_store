from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View
from app_market.utils import get_all_books, get_catalog_books, search_books_and_authors
from app_market.models import Book


class HomeView(TemplateView):
    """Главная страница"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = get_all_books()
        context['popular_list'] = get_all_books()[:8]
        return context


class BookView(DetailView):
    """Просмотр информации о конкретной книге"""
    model = Book
    template_name = 'book.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        context['image'] = book.image.first()
        context['author'] = f'{book.author.profile.first_name} {book.author.profile.last_name}'
        context['genres'] = book.genre.all()
        context['tags'] = book.tags.all()
        context['cycle'] = book.cycle
        return context


class CatalogView(View):
    """Каталог книг"""
    def get(self, request):
        search = request.GET.get('search')
        if search:
            return render(request, 'catalog.html', context=search_books_and_authors(search))
        return render(request, 'catalog.html', context=get_catalog_books(request))
