# Generated by Django 4.2.7 on 2023-11-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.CharField(default='Москва', max_length=100, verbose_name='создано в '),
        ),
    ]
