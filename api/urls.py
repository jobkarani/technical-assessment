from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_dataset1/', views.create_dataset1, name='create_dataset1'),
    path('dataset1/', views.dataset1, name='dataset1'),
    path('api/dataset1/', views.Dataset1List.as_view()),

    path('create_dataset2/', views.create_dataset2, name='create_dataset2'),
    path('dataset2/', views.dataset2, name='dataset2'),
    path('api/dataset2/', views.Dataset2List.as_view()),

    path('create_dataset3/', views.create_dataset3, name='create_dataset3'),
    path('dataset3/', views.dataset3, name='dataset3'),
    path('api/dataset3/', views.Dataset3List.as_view()),

    path('api/datasets/', views.DatasetList.as_view()),
]