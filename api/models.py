from django.db import models
import datetime
from app import *
from django.contrib.postgres.fields import ArrayField


DATE_INPUT_FORMATS = ['%Y-%d-%m']
# Create your models here.
class  Dataset1(models.Model):
    dob = models.DateField(editable=DATE_INPUT_FORMATS,null=True)
    email = models.EmailField(max_length=256, null=True)
    idNumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    def save_dataset1(self):
        self.save()

    def delete_dataset1(self):
        self.save()

    def update(self):
        self.save()

    def __str__(self):
        return self.name

class  Dataset2(models.Model):
    dob = models.DateField(editable=DATE_INPUT_FORMATS,null=True)
    idNumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = ArrayField(models.CharField(null=True,blank=True),null=True,blank=True)

    def save_dataset2(self):
        self.save()

    def delete_dataset2(self):
        self.save()

    def update(self):
        self.save()

    def __str__(self):
        return self.name

class  Dataset3(models.Model):
    grade = models.CharField(max_length=2)
    probability = models.FloatField()

    def save_dataset3(self):
        self.save()

    def delete_dataset3(self):
        self.save()

    def update(self):
        self.save()

    def __str__(self):
        return self.grade
