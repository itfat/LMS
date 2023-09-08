from django.db import models

from library.BaseModel import BaseModel

# Create your models here.

class User(BaseModel):
    name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=300)
    password = models.CharField(max_length=30)


    def __str__(self):
        return self.name
