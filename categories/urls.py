from django.urls import path
from .views import CategoryListAPIView, CategoryCreateAPIView, CategoryDetailAPIView
from spendings.views import SpendingListAPIView
from spendings.count import CategorysTotalSumAPIView, CategoryTotalSumListAPIView, SpendingsByRangeAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', SpendingListAPIView.as_view()),
    path('categories/<int:category_id>/total_sum/', CategorysTotalSumAPIView.as_view()),
    path('categories/total_sum_list/', CategoryTotalSumListAPIView.as_view()),

    path('categories/create/', CategoryCreateAPIView.as_view()),
    path('categories/<int:category_id>/detail/', CategoryDetailAPIView.as_view()),

    path('categories/<int:category_id>/filter/', SpendingsByRangeAPIView.as_view())

]
