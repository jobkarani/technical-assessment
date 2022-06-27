from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['dob', 'email', 'idNumber','name','phone','grade','probability']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dob', 'email', 'idNumber','name','phone','grade','probability']

