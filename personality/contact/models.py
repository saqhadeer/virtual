from django.db import models
from django.contrib.auth.models import User

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=25)
    message = models.TextField(max_length=500)



    def __str__(self):
        return self.email








