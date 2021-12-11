from django_filters import rest_framework as filters


class SpendingFilterByDate(filters.FilterSet):
    start_date = filters.DateFilter(field_name="created_at__date", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="created_at__date", lookup_expr="lte")


class SpendingFilterByDay(filters.FilterSet):
    choosen_day = filters.DateFilter(field_name="created_at__date", lookup_expr="exact")