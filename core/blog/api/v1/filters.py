from django_filters import rest_framework as filters
from blog.models import Post


class PostFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="published_date", lookup_expr='gte', label='from date')
    to_date = filters.DateFilter(field_name="published_date", lookup_expr='lte', label='to date')

    class Meta:
        model = Post
        fields = ['category', 'title', 'from_date', 'to_date']