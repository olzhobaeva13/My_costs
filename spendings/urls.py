from django.urls import path
from .views import SpendingCreateAPIView, SpendingDetailAPIView
from .count import TodaySpendingsListAPIView, AllSpendingsListAPIView, TodaysTotalSumAPIView, SpendingsByDayAPIView

urlpatterns = [
    path('spendings/', AllSpendingsListAPIView.as_view()),
    path('spendings/create/', SpendingCreateAPIView.as_view()),
    path('spendings/<int:spending_id>/detail/', SpendingDetailAPIView.as_view()),

    path('spendings/today_list/', TodaySpendingsListAPIView.as_view()),
    path('spendings/todays_total_sum/', TodaysTotalSumAPIView.as_view()),

    path('spendings/filter/', SpendingsByDayAPIView.as_view()),

]