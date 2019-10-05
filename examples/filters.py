from django_filters import FilterSet

from .models import equipment


class EqFilter(FilterSet):
    class Meta:
        model = equipment
        fields = {"name": ["exact", "contains"], "type": ["exact"]}
