from rest_framework import serializers
from .models import Spending

class SpendingSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')
    class Meta:
        
        model = Spending
        fields = ['id', 'category', 'summ', 'created_at', 'owner',]
        read_only_fields = ['created_at', 'owner']