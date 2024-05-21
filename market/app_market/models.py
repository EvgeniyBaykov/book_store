from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Book(models.Model):
    """Класс описывающий книгу"""
    title = models.CharField(max_length=100, db_index=True, verbose_name=_('Название книги'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', verbose_name=_('Автор'))
    description = models.CharField(max_length=1000, null=True, default='', verbose_name=_('Описание'))
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_('цена'))
    tags = models.ManyToManyField('Tag', default=None, related_name='books', blank=True, verbose_name=_('теги'))
    genre = models.ManyToManyField('Genre', default=None, related_name='books', verbose_name=_('жанр'))
    create_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('Дата создания'))
    update_date = models.DateTimeField(null=True, auto_now=True, verbose_name=_('Дата редактирования'))
    slug = models.SlugField(verbose_name=_('Название ссылки'))

    class Meta:
        verbose_name = _('Книга')
        verbose_name_plural = _('Книги')

    def __str__(self):
        return f'{self.author} - {self.title}'


class Tag(models.Model):
    """Класс описывающий теги"""
    tag = models.CharField(max_length=200, blank=True, verbose_name=_('Теги'))

    class Meta:
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')

    def __str__(self):
        return self.tag


class Genre(MPTTModel):
    """Класс описывающий жанры книг"""
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Название жанра'))
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='subgenre',
                            db_index=True, verbose_name=_('Родительский жанр'))
    slug = models.SlugField(verbose_name=_('Название ссылки'))

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')

    def __str__(self):
        return self.name


class BookImage(models.Model):
    """Модель обложки к книге"""
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='image', verbose_name=_('Книга'))
    image = models.ImageField(upload_to='images/books/%Y/%m', verbose_name=_('Обложка книги'))
    image_alt = models.CharField(max_length=100, default=_('Обложка книги'), verbose_name=_('Подсказка'))

    class Meta:
        verbose_name = _('Обложка')
        verbose_name_plural = _('Обложки')

