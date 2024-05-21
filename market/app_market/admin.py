from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from app_market.models import (
    Book,
    Tag,
    Genre,
    BookImage
)


class BookImageInline(admin.TabularInline):
    model = BookImage
    max_num = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['id', 'title', 'author', 'price', 'create_date', 'update_date']
    search_fields = ['title', 'author', 'tags']
    list_filter = ['genre']
    prepopulated_fields = {'slug': ('author', 'title')}
    inlines = [BookImageInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['id', 'tag']


@admin.register(Genre)
class GenreAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("name",)}
