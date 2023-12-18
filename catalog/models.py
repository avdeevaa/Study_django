from django.db import models
from django.utils.text import slugify

from config import settings


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='catalog/images/', verbose_name='изображение (превью)', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    creation_date = models.DateField(verbose_name='дата создания')
    modification_date = models.DateField(verbose_name='дата последнего изменения')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")

    number_of_version = models.IntegerField(verbose_name='номер версии')
    name_of_version = models.CharField(max_length=100, verbose_name='название версии')
    is_active_version = models.BooleanField(verbose_name="признак текущей версии", default=True)

    def __str__(self):
        if self.is_active_version == True:
            return f"{self.name_of_version}, {self.number_of_version}"

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ('name',)


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', unique=True, blank=True)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='catalog/images/', verbose_name='изображение (превью)', null=True, blank=True)
    creation_date = models.DateField(verbose_name='дата создания')

    publication_sign = models.BooleanField(default=True, verbose_name="признак публикации", null=True, blank=True)
    number_of_views = models.PositiveIntegerField(default=0, verbose_name="количество просмотров")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}: {self.content}"

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"

