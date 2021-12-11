from django.db import models
from categories.models import Category
from django.contrib.auth import get_user_model


User = get_user_model()

class Spending(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spendings')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='spendings')
    summ = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    