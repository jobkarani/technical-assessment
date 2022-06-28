from django.db import models
import datetime
from app import *
from django.contrib.postgres.fields import ArrayField


DATE_INPUT_FORMATS = ['%Y-%d-%m']
# Create your models here.
class  Profile(models.Model):
    dob = models.DateField(editable=DATE_INPUT_FORMATS,blank=True,default=None,null=True)
    email = models.EmailField(max_length=256,blank=True,default=None, null=True)
    idNumber = models.CharField(max_length=100,blank=True,default=None, null=True)
    name = models.CharField(max_length=100,blank=True,default=None, null=True)
    phone = ArrayField(models.CharField(max_length=12,default=None,null=True,blank=True),default=None,null=True,blank=True)
    grade = models.CharField(max_length=2,blank=True, default=None,null=True)
    probability = models.FloatField(blank=True,default=None, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    def update(self):
        self.save()

    