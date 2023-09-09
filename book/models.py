from django.db import models
from library.BaseModel import BaseModel
from user.models import CustomUser

# Create your models here.

class Book(BaseModel):
    STATUS = [
        ("AVAILABLE", "Available"),
        ("ON_HOLD", "on_hold")
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_year = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default="AVAILABLE")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="the user who has book", null=True)

