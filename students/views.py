from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def students(request):
    students = [
        {'id': 1, 'name': 'ahmed', 'age': 20},  
        {'id': 2, 'name': 'nuur', 'age': 22},    
        {'id': 3, 'name': 'cole', 'age': 23},]
    return HttpResponse(students)
