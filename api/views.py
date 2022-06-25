from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .serializer import *
from rest_framework.views import APIView

# Create your views here.
def index(request):

    return render(request, "index.html")

def create_profile(request):
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'createProfile.html', {"form": form, "title": title})



def profile(request):
    profile = Profile.objects.all()

    return render(request, "profile.html", {"profile": profile})

class ProfileList(APIView):

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
