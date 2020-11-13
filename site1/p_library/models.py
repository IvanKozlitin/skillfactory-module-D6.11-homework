import time

from django.db import models


class Author(models.Model):
    full_name = models.TextField(verbose_name="Имя")
    birth_year = models.SmallIntegerField(verbose_name="Год рождения")
    country = models.CharField(verbose_name="Страна", max_length=2)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.full_name


class PublishingHouse(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    phone = models.CharField(max_length=16, verbose_name="Телефон")
    email = models.EmailField(null=True, blank=True, verbose_name="Email")
    city = models.TextField(null=True, blank=True, verbose_name="Город")
    foundation_date = models.SmallIntegerField(null=True, blank=True, verbose_name="Дата основания")
    country = models.CharField(max_length=2, verbose_name="Страна")
    works = models.NullBooleanField(verbose_name="Работает ли издательство")

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name


class Friend(models.Model):
    full_name = models.TextField(verbose_name="Имя")
    birth_year = models.SmallIntegerField(verbose_name="Год рождения")
    phone = models.CharField(max_length=16, blank=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    year_release = models.SmallIntegerField(verbose_name="Год публикации")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", verbose_name="Автор")
    p_house = models.ForeignKey(PublishingHouse, on_delete=models.SET_NULL, null=True, blank=True, related_name="books",
                                verbose_name="Издательство")
    copy_count = models.SmallIntegerField(default=1, verbose_name="Количество копий")
    price = models.FloatField(verbose_name="Стоимость")
    image = models.ImageField(upload_to='books_images/%Y/%m/%d', blank=True, verbose_name='Ссылка картинки')
    friends = models.ManyToManyField(
        Friend,
        through='WhenTook',
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

# Вывод картинок в админке!
    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="60"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class WhenTook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, verbose_name="Друг")
    when_took = models.DateField(verbose_name="Какого числа была взята книга")

    class Meta:
        verbose_name = 'Книга у друга'
        verbose_name_plural = 'Книги у друзей'

    def __str__(self):
        return "Книгу '{}' взял мой друг '{}', {}".format(
            self.book, self.friend, time.strftime("%d.%m.%Y", time.strptime(self.when_took.ctime())))
