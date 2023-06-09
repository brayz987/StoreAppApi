from django.db import models
from django.contrib.auth.models import AbstractUser


# Modify user default model

class CustomUserModel(AbstractUser):
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name}'


