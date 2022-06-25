from http.client import PROCESSING
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response 

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
    return render(request, 'createDataset1.html', {"form": form, "title": title})



def dataset1(request):
    dataset1 = Dataset1.objects.all()
    dataset2= Dataset2.objects.all()
    dataset3= Dataset3.objects.all()

    return render(request, "dataset1.html", {"dataset1": dataset1,"dataset2": dataset2,"dataset3": dataset3})


def create_dataset2(request):
    title = "Create Dataset2"
    if request.method == 'POST':
        form = Dataset2Form(request.POST, request.FILES)
        if form.is_valid():
            dataset2 = form.save(commit=False)
            dataset2.save()
        return HttpResponseRedirect('/')

    else:
        form = Dataset2Form()
    return render(request, 'createDataset2.html', {"form": form, "title": title})



def dataset2(request):
    dataset2 = Dataset2.objects.all()

    return render(request, "dataset2.html", {"dataset2": dataset2})

def create_dataset3(request):
    title = "Create Dataset3"
    if request.method == 'POST':
        form = Dataset3Form(request.POST, request.FILES)
        if form.is_valid():
            dataset3 = form.save(commit=False)
            dataset3.save()
        return HttpResponseRedirect('/')

    else:
        form = Dataset3Form()
    return render(request, 'createDataset3.html', {"form": form, "title": title})



def dataset3(request):
    dataset3 = Dataset3.objects.all()

    return render(request, "dataset3.html", {"dataset3": dataset3})




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



def grade(grade):
    if grade == 'AA':
        grade = 1
    elif grade=='BB':
        grade =0.9
    elif grade == 'CC':
        grade = 0.8
    elif grade == 'DD':
        grade = 0.7
    elif grade == 'EE':
        grade = 0.6
    elif grade == 'GG':
        grade = 0.5
    elif grade == 'FF':
        grade = 0.4
    
    return grade 

print(grade('FF'))