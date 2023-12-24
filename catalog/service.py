from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


class CategoryService:
    @staticmethod
    def cache_example():
        if CACHE_ENABLED:
            key = f'all_categories'
            all_categories = cache.get(key)
            if all_categories is None:
                all_categories = Category.objects.all()
                cache.set(key, all_categories)
        else:
            all_categories = Category.objects.all()
        return all_categories
