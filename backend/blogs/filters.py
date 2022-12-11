import django_filters
from blogs.models import Category,Post


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'category': ['exact'],
            'author': ['exact'],
            
        }


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'name': ['exact']
        }



