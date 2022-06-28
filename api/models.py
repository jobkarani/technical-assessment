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

# class Dataset1:
#     def __init__(self, dob, email, idNumber,name,phone):
#         self.dob = dob
#         self.email = email
#         self.idNumber =idNumber
#         self.name = name
#         self.phone = phone

# dataset1 = Dataset1(dob='2000-20-7', email='johndoe@gmail.com', idNumber='12345678', name='John Doe' , phone='254711000001')

# class Dataset2:
#     def __init__(self, dob, idNumber,name,phone):
#         self.dob = dob
#         self.idNumber =idNumber
#         self.name = name
#         self.phone = phone

# dataset2 = Dataset2(dob='2000-20-7', idNumber='12345678', name='John Doe' , phone=['254711000001','254711000002'])

# class Dataset3:
#     def __init__(self, grade, probability):
#         self.grade = grade
#         self.probability =probability

# dataset3 = Dataset3(grade='BB', probability='3.8')