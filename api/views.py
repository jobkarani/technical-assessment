from django.shortcuts import redirect, render
from .models import *
from .forms import *
from rest_framework import status
from django.http import Http404
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import generics

# Create your views here.
def create_profile(request):
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        # return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})



def profile(request):
    profile = Profile.objects.all()

    return render(request, "profile.html", {"profile": profile})

def update_profile(request, id):
    profile = Profile.objects.all()
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')

    ctx = {"form": form}
    return render(request, 'update_prof.html', ctx)


class ProfileList(APIView):
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'profiles': reverse('ProfileList', request=request, format=format)
    })

class ProfileHighlight(generics.GenericAPIView):
    queryset = Profile.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        return Response(profile.highlighted)


# def compare_name(request,name):
    
#     name2 = Dataset2.objects.get(name=name)
#     name1 = Dataset1.objects.get(name=name)
#     if name2 != name1:
#         name = 0
#     else:
#         name = name2

#     return render(request, 'index.html')

# def compare_phone(request,phone):
    
#     phone1 = Dataset1.objects.get(phone=phone)
#     phone2 = Dataset2.objects.get(phone=phone)
#     if phone1 != phone2:
#         phone = 0
#     else:
#         phone = phone1

#     return render(request, 'index.html')

# def compare_dob(request,dob):
    
#     dob1 = Dataset1.objects.get(dob=dob)
#     dob2 = Dataset2.objects.get(dob=dob)
#     if dob1 != dob2:
#         dob = 0
#     else:
#         dob = dob1

#     return render(request, 'index.html')

# def compare_email():
#     email1 = Dataset1.objects.filter(email=request.email)
#     email2 = Dataset2.objects.filter(email=request.email)
#     if email1 != email2:
#         email = -10
#     else:
#         email = email1

#     return email1

# print(compare_email())

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