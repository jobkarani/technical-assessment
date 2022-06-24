from django.db import models
from django.db.models import Model

# Create your models here.
class  Profile(models.Model):
    dob = models.DateTimeField(null=True)
    email = models.EmailField(max_length=256, null=True)
    idNumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    grade = models.CharField(max_length=2)
    probability = models.FloatField()
