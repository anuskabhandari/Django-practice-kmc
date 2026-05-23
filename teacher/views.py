from django.http import HttpResponse
from django.shortcuts import redirect, render

from teacher.forms import TeacherForm
from teacher.models import Teacher

# Create your views here.
def teacher_list(request):
    data = Teacher.objects.all()
    context = {
        "teacher":data
    }
    return render(request, 'teacher/index.html', context)



def create_teacher(request):
    teacher_form = TeacherForm()
    if request.method == "POST":
        teacher_form = TeacherForm(data=request.POST)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('/grade/teacher')
    context = {
        "form":teacher_form
    }
    return render(request,'teacher/create.html', context)