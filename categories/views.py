from rest_framework import status, generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from spendings.count import CategorysTotalSumAPIView


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ]
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CategoryDetailAPIView(APIView):

    permission_classes = [IsAuthenticated, ]
    
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id, owner=self.request.user)
        serializer = CategorySerializer(instance=category)
        return Response(serializer.data)

    def put(self, request, category_id):
        category = get_object_or_404(Category, id=category_id, owner=self.request.user)
        serializer = CategorySerializer(instance=category, data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            category.name = name
            category.save()
            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category = get_object_or_404(Category, id=category_id, owner=self.request.user)
        category.delete()
        return Response({'detail': 'success'}, status=status.HTTP_204_NO_CONTENT)
