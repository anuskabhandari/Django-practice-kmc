from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from home.forms import StudentForm
from home.models import Student
# Create your views here.
def home(request):
    print("Hello from django!!")
    return HttpResponse("<u> Hello from djangooooo </u>")

def home__json(request):
    data ={
        "name" : "MY NAME",
        "address" : "Kanchanpur"
        }
    return JsonResponse(data)

def landing_page(request):
    user_info ={
        "name": "Anuska Bhandari"
    }
    return render(request,'home/index.html', user_info)


def student_list(request):
    student = Student.objects.all()
    context ={
        "student" : student
    }
    return render(request, 'student/index.html', context)

def student_create(request):
    if request.method == "POST":
        print(request.POST)
        data = request.POST
        Student.objects.create(
            name = data['student_name'],
            contact_number = data['number'],
            dob = data['dob']
        )
        return redirect('/home/student_list')

    return render(request, 'student/create.html')

def student_create2(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/student_list')
        else:
            print(form.errors)
    context = {
        "form":form
    }
    return render(request, 'student/create2.html', context)

def student_update(request,id):
    print("this is id from url", id)
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/home/student_list')
        else:
            print(form.errors)
    context = {
        "form":form
    }
    return render(request, 'student/update.html', context)

def student_delete(request , id):
    student = Student.objects.filter(id=id).delete()
    return redirect('/home/student_list')
