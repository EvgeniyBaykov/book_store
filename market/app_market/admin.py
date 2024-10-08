from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from django.utils.translation import gettext_lazy as _

from app_market.models import (
    Book,
    Tag,
    Genre,
    Cycle,
    BookImage,
    BookReview,
    BookReviewImage
)


class BookImageInline(admin.TabularInline):
    model = BookImage
    max_num = 1


class BookReviewImageInline(admin.TabularInline):
    model = BookReviewImage
    max_num = 3


class BookTagInLine(admin.TabularInline):
    model = Book.tags.through


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['id', 'title', 'author_name', 'price', 'create_date', 'update_date']
    search_fields = ['title', 'author', 'tags']
    list_filter = ['genre']
    prepopulated_fields = {'slug': ('author', 'title')}
    inlines = [BookImageInline, BookTagInLine, ]
    exclude = ["tags"]

    @admin.display(description=_('Автор'))
    def author_name(self, obj):
        last_name = obj.author.profile.last_name
        if last_name:
            name = f'{obj.author.profile.first_name} {last_name}'
        else:
            name = f'{obj.author.profile.first_name}'
        return name


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # model = Tag
    list_display = ['id', 'tag']
    inlines = [BookTagInLine,]


@admin.register(Genre)
class GenreAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    model = Cycle
    list_display = ['id', 'name', 'author_name', 'create_date', 'update_date', 'completed']
    search_fields = ['name', 'author', 'completed']
    prepopulated_fields = {"slug": ("name",)}

    @admin.display(description=_('Автор'))
    def author_name(self, obj):
        last_name = obj.author.profile.last_name
        if last_name:
            name = f'{obj.author.profile.first_name} {last_name}'
        else:
            name = f'{obj.author.profile.first_name}'
        return name


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    model = BookReview
    list_display = ['id', 'user', 'create_date', 'description_short']
