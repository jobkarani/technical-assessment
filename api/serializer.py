from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ('dob', 'email', 'idNumber','name','phone','grade','probability')



# class Dataset1Serializer(serializers.Serializer):
#     dob = serializers.DateField()
#     email = serializers.EmailField()
#     idNumber = serializers.CharField(max_length=10)
#     name = serializers.CharField(max_length=100)
#     phone = serializers.CharField(max_length=12)

# serializer = Dataset1Serializer(dataset1)
# serializer.data

# class Dataset2Serializer(serializers.Serializer):
#     dob = serializers.DateField()
#     idNumber = serializers.CharField(max_length=10)
#     name = serializers.CharField(max_length=100)
#     phone = serializers.CharField(max_length=12)

# serializer = Dataset2Serializer(dataset2)
# serializer.data

# class Dataset3Serializer(serializers.Serializer):
#     grade = serializers.CharField(max_length=2)
#     probability = serializers.FloatField()

# serializer = Dataset3Serializer(dataset3)
# serializer.data

# json = JSONRenderer().render(serializer.data)
# json
