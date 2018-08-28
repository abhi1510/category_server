import django_filters

from product.models import Category


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ('is_featured', 'is_active')
