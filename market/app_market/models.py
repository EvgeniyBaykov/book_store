from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Book(models.Model):
    """Класс описывающий книгу"""
    title = models.CharField(max_length=100, db_index=True, verbose_name=_('название книги'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', verbose_name=_('автор'))
    description = models.CharField(max_length=2000, null=True, default='', verbose_name=_('описание'))
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_('цена'))
    tags = models.ManyToManyField('Tag', default=None, related_name='books', blank=True, verbose_name=_('теги'))
    genre = models.ManyToManyField('Genre', default=None, related_name='books', verbose_name=_('жанр'))
    cycle = models.ForeignKey('Cycle', on_delete=models.CASCADE, null=True, blank=True, related_name='books',
                              verbose_name=_('цикл'))
    authors_note = models.CharField(max_length=2000, null=True, blank=True, verbose_name=_('примечание автора'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'))
    update_date = models.DateTimeField(null=True, auto_now=True, verbose_name=_('дата редактирования'))
    slug = models.SlugField(verbose_name=_('название ссылки'))

    class Meta:
        verbose_name = _('Книга')
        verbose_name_plural = _('Книги')

    def __str__(self):
        return f'{self.author.profile.first_name} {self.author.profile.last_name} - {self.title}'


class Tag(models.Model):
    """Класс описывающий теги"""
    tag = models.CharField(max_length=200, blank=True, verbose_name=_('теги'))

    class Meta:
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')

    def __str__(self):
        return self.tag


class Genre(MPTTModel):
    """Класс описывающий жанры книг"""
    name = models.CharField(max_length=100, unique=True, verbose_name=_('название жанра'))
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='subgenre',
                            verbose_name=_('родительский жанр'))
    slug = models.SlugField(verbose_name=_('название ссылки'))

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
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='image', verbose_name=_('книга'))
    image = models.ImageField(upload_to='images/books/%Y/%m', verbose_name=_('обложка книги'))
    image_alt = models.CharField(max_length=100, default=_('Обложка книги'), verbose_name=_('подсказка'))

    class Meta:
        verbose_name = _('Обложка')
        verbose_name_plural = _('Обложки')


class Cycle(models.Model):
    """Модель описывающая цикл книг"""
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name=_('название цикла'))
    description = models.CharField(max_length=2000, verbose_name=_('описание цикла'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cycles', verbose_name=_('автор'))
    create_date = models.DateField(auto_now_add=True, verbose_name=_('дата создания'))
    update_date = models.DateField(null=True, auto_now=True, verbose_name=_('дата редактирования'))
    completed = models.BooleanField()
    slug = models.SlugField(verbose_name=_('название ссылки'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Цикл')
        verbose_name_plural = _('Циклы')


class BookReview(models.Model):
    """Модель описывающая отзывы к книге"""
    user = models.ForeignKey(User, on_delete=models.SET('Deleted'), related_name='book_reviews',
                             verbose_name=_('пользователь'))
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='book_reviews', verbose_name=_('книга'))
    description = models.TextField(max_length=2000, verbose_name=_('текст комментария'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('дата написания'))

    def description_short(self):
        """
        Функция возвращает описание, если его длина меньше 15 символов, иначе возвращает
        срез первых 15 символов с многоточием.
        :return: Обрезанное описание.
        """
        if len(self.description) > 15:
            return self.description[:15] + '...'
        return self.description

    def __str__(self):
        return f'Запись: {self.description_short()}, Пользователь: {self.user}'

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')


class BookReviewImage(models.Model):
    """Модель картинок, которые пользователи добавляют к комментариям книг"""
    review = models.ForeignKey('BookReview', on_delete=models.CASCADE, related_name='image', verbose_name=_('отзыв'))
    image = models.ImageField(upload_to='images/books/%Y/%m', verbose_name=_('картинка'))
    image_alt = models.CharField(max_length=100, default=_('Изображение к отзыву'), verbose_name=_('подсказка'))

    class Meta:
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')
