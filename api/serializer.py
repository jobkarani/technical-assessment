from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ('dob', 'email', 'idNumber','name','phone','grade','probability')

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
