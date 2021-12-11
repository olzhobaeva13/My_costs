from datetime import date
from rest_framework import generics, views
from spendings.models import Spending
from spendings.serializers import SpendingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from categories.models import Category
from django_filters import rest_framework as filters
from .filters import SpendingFilterByDate, SpendingFilterByDay

today = date.today()

class TodaySpendingsListAPIView(generics.ListAPIView):
    serializer_class = SpendingSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Spending.objects.filter(created_at__gte=today, owner=self.request.user)

class TodaysTotalSumAPIView(views.APIView):
    serializer_class = SpendingSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        total_sum = 0
        for spending in Spending.objects.filter(created_at__gte=today, owner=self.request.user):
            total_sum += spending.summ
        return Response(total_sum)


class AllSpendingsListAPIView(generics.ListAPIView):
    queryset = Spending.objects.all()
    serializer_class = SpendingSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CategorysTotalSumAPIView(views.APIView):
    serializer_class = SpendingSerializer
    permission_classes = [IsAuthenticated, ]


    def get(self, request, category_id):
        total_sum = 0
    
        for spending in Spending.objects.filter(category_id=self.kwargs.get('category_id'), owner=self.request.user):
            total_sum += spending.summ
        return Response(total_sum)


class CategoryTotalSumListAPIView(views.APIView):
    serializer_classes = SpendingSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        categories_list = []
        sums_list = []
        for category in Category.objects.filter(owner=self.request.user):
            categories_list.append(category.name)
            total_sum = 0
            for spending in Spending.objects.filter(owner=self.request.user, category_id=category.id):
                total_sum += spending.summ
            sums_list.append(total_sum)
        total_sum_dict = zip(categories_list, sums_list)

        return Response(total_sum_dict)


class SpendingsByRangeAPIView(generics.ListAPIView): 
    queryset = Spending.objects.all()
    serializer_class = SpendingSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = SpendingFilterByDate

    def get_queryset(self):
        return self.queryset.filter(category_id=self.kwargs.get('category_id'), owner=self.request.user)


class SpendingsByDayAPIView(generics.ListAPIView):
    queryset = Spending.objects.all()
    serializer_class = SpendingSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = SpendingFilterByDay

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)