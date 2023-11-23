from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение (превью)', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    creation_date = models.DateField(verbose_name='дата создания')
    modification_date = models.DateField(verbose_name='дата последнего изменения')
    created_at = models.CharField(default="Москва", max_length=100, verbose_name='создано в ')

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ('name',)