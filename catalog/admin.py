from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class Version(admin.ModelAdmin):
    list_display = ('number_of_version', 'name_of_version', 'is_active_version',)


