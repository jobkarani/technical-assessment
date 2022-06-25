# import serializer from rest_framework
from rest_framework import serializers
from .models import *


class Dataset1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset1
        fields = ('dob', 'email', 'idNumber','name','phone')

class Dataset2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset2
        fields = ('dob', 'idNumber','name','phone')

class Dataset3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset3
        fields = ('grade','probability')