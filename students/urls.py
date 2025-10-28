from django.urls import path
from . import views

urlpatterns = [
    path('', views.students),  # GET all students or POST a new student    
]