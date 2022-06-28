from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('createprofile/', views.create_profile, name='create_profile'),
    path('api/profiles/', views.ProfileList.as_view()),
    # path('Dataset1Serializer/', views.Dataset1Serializer, name='Dataset1Serializer'),
]
