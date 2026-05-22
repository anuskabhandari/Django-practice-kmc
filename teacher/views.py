from django.http import HttpResponse
from django.shortcuts import render

from teacher.models import Teacher

# Create your views here.
def teacher_list(request):
    data = Teacher.objects.all()
    context = {
        "teacher":data
    }
    return render(request, 'teacher/index.html', context)