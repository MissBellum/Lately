from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('LatelyFit/', views.index, name='latelyfit'),
    path('test/', views.test, name='test'),
]
