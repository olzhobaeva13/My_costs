from django import views
from rest_framework import generics, serializers

from spendings.models import Spending
from spendings.serializers import SpendingSerializer
from categories.models import Category
from categories.serializers import CategorySerializer

class DraftAPIView(generics.ListAPIView):
    serializer_class = SpendingSerializer

    def get_queryset(self):
        return Spending.objects.filter(owner=5)
