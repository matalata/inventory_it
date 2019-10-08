from django_filters import FilterSet

from .models import equipment


class EqFilter(FilterSet):
    class Meta:
        model = equipment
        fields = {"type": ["exact"], "dep": ["exact"]}
