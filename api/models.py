from django.db import models
import datetime as dt

# Create your models here.
class  Profile(models.Model):
    dob = models.DateField(null=True)
    email = models.EmailField(max_length=256, null=True)
    idNumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    grade = models.CharField(max_length=2)
    probability = models.FloatField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    def update(self):
        self.save()

    def __str__(self):
        return self.name
