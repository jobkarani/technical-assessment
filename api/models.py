from django.db import models
import datetime
from app import *
from django.contrib.postgres.fields import ArrayField


DATE_INPUT_FORMATS = ['%Y-%d-%m']
# Create your models here.
class  Profile(models.Model):
    dob = models.DateField(editable=DATE_INPUT_FORMATS,blank=True,null=True)
    email = models.EmailField(max_length=256,blank=True, null=True)
    idNumber = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    phone = ArrayField(models.CharField(max_length=12,null=True,blank=True),null=True,blank=True)
    grade = models.CharField(max_length=2,blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    def update(self):
        self.save()

    