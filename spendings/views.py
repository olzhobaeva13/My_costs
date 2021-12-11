from rest_framework import status, generics
from .models import Spending
from .serializers import SpendingSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class SpendingCreateAPIView(generics.CreateAPIView ):
    queryset = Spending.objects.all()
    serializer_class = SpendingSerializer
    permission_classes = [IsAuthenticated, ]
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class SpendingListAPIView(generics.ListAPIView):
    serializer_class = SpendingSerializer
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        return Spending.objects.filter(category_id=self.kwargs.get('category_id'))


class SpendingDetailAPIView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request, spending_id):
        spending = get_object_or_404(Spending, id=spending_id, owner=self.request.user)
        serializer = SpendingSerializer(instance=spending)
        return Response(serializer.data)

    def put(self, request, spending_id):
        spending = get_object_or_404(Spending, id=spending_id, owner=self.request.user)
        serializer = SpendingSerializer(instance=spending, data=request.data)

        if serializer.is_valid():
            category = serializer.validated_data.get('category')
            summ = serializer.validated_data.get('summ')
            spending.category = category
            spending.summ = summ
            spending.save()
            
            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, spending_id):
        spending = get_object_or_404(Spending, id=spending_id, owner=self.request.user)
        spending.delete()
        return Response({'detail': 'success'}, status=status.HTTP_204_NO_CONTENT)
