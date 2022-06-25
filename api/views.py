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

def create_dataset1(request):
    title = "Create Dataset1"
    if request.method == 'POST':
        form = Dataset1Form(request.POST, request.FILES)
        if form.is_valid():
            dataset1 = form.save(commit=False)
            dataset1.save()
        return HttpResponseRedirect('/')

    else:
        form = Dataset1Form()
    return render(request, 'createProfile.html', {"form": form, "title": title})



def dataset1(request):
    dataset1 = Dataset1.objects.all()

    return render(request, "profile.html", {"dataset1": dataset1})




class Dataset1List(APIView):

    def get(self, request, format=None):
        dataset1 = Dataset1.objects.all()
        serializer = Dataset1Serializer(dataset1, many=True)
        return Response(serializer.data)


class Dataset2List(APIView):

    def get(self, request, format=None):
        dataset2 = Dataset2.objects.all()
        serializer = Dataset2Serializer(dataset2, many=True)
        return Response(serializer.data)
        

class Dataset3List(APIView):

    def get(self, request, format=None):
        dataset3 = Dataset3.objects.all()
        serializer = Dataset3Serializer(dataset3, many=True)
        return Response(serializer.data)
