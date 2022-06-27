# import serializer from rest_framework
from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('dob', 'email', 'idNumber','name','phone','grade','probability')