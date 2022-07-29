from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("snack_detail", args=[self.id])
