from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('createprofile/', views.create_profile, name='create_profile'),
    path('api/profiles/', views.ProfileList.as_view()),
]