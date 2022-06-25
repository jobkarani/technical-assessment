# import serializer from rest_framework
from rest_framework import serializers
from .models import *


class Dataset1Serializer(serializers.ModelSerializer):
    class Dataset2Serializer(serializers.ModelSerializer):
        class Meta:
            model = Dataset2
            fields = ('dob', 'idNumber','name','phone')
    dataset2 = Dataset2Serializer()

    class Dataset3Serializer(serializers.ModelSerializer):
        class Meta:
            model = Dataset3
            fields = ('grade','probability')
    dataset3 = Dataset3Serializer()

    class Meta:
        model = Dataset1
        fields = ('dob', 'email', 'idNumber','name','phone')

    def create(self, validated_data):
            dataset2_data = validated_data.pop('dataset2')
            dataset3_data = validated_data.pop('dataset3')
            dataset1_instance = Dataset1.objects.create(**validated_data)
            Dataset2.objects.create(dob=dataset1_instance,
                                idNumber=dataset1_instance,
                                name=dataset1_instance,
                                phone=dataset1_instance,
                                **dataset2_data)
            Dataset3.objects.create(grade=dataset1_instance,
                                probability=dataset1_instance,
                                **dataset3_data)                   
            return dataset1_instance
    