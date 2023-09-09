from django.db import models

from django.contrib.auth.models import User

class CustomUser(User):
    ROLES = [
        ("NORMAL", "Normal"),
        ("MANAGERr", "Manager"),
        ("ADMIN", "Admin"),
    ]

    role = models.CharField(max_length=10, choices=ROLES, default="NORMAL")

