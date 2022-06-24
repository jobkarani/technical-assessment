from rest_framework.response import Response
from .models import *
from api import serializer
from .serializer import *
from rest_framework.views import APIView

# Create your views here.
class ProfileList(APIView):

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
