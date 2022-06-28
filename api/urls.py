from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('profiles/highlight/', views.ProfileHighlight.as_view()),
    path('profile/', views.profile, name='profile'),
    path('createprofile/', views.create_profile, name='create_profile'),
    path('api/profiles/', views.ProfileList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)