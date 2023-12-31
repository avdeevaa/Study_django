# Generated by Django 4.2.7 on 2023-12-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='catalog/images/', verbose_name='изображение (превью)')),
                ('creation_date', models.DateField(verbose_name='дата создания')),
                ('publication_sign', models.BooleanField(default=False, verbose_name='признак публикации')),
                ('number_of_views', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Запись блога',
                'verbose_name_plural': 'Записи блога',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/images/', verbose_name='изображение (превью)'),
        ),
    ]
