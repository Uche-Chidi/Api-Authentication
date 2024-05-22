from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=155, unique=True)
    # phone_number = models.IntegerField(max_length=155)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.email

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    names=models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    email=models.EmailField(max_length=200)
    address=models.TextField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    # website=models.URLField()
    # price=models.DecimalField()

    def __str__(self) -> str:
        return self.names
