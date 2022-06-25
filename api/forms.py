from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *


class Dataset1Form(ModelForm):
    class Meta:
        model = Dataset1
        fields = ['dob', 'email', 'idNumber','name','phone']

class Dataset2Form(ModelForm):
    class Meta:
        model = Dataset2
        fields = ['dob', 'idNumber','name','phone']

class Dataset3Form(ModelForm):
    class Meta:
        model = Dataset3
        fields = ['grade', 'probability']