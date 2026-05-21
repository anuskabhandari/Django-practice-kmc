from django.http import HttpResponse
from django.shortcuts import render

from teacher.models import Teacher

# Create your views here.

def teacher_list(request):
    teacher = Teacher.objects.all()
    context ={
        "teacher" : teacher
    }
    return render(request, 'home/index.html', context)