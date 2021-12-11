from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
