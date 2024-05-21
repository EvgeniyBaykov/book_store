from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from app_market.utils import get_all_books
from app_market.models import Book


class HomeView(TemplateView):
    """Главная страница"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = get_all_books()
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
        context['author'] = 'authors name'
        context['genres'] = book.genre.all()
        context['tags'] = book.tags.all()
        return context
