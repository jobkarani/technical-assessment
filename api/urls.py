from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('api/profiles/', views.ProfileList.as_view()),
]