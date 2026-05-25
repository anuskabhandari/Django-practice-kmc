from django.shortcuts import redirect, render

# Create your views here.

from user.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(request.POST['password'])
            form.save()
            return redirect('/admin')
        else:
            print(form.errors)
    context = {
        "form":form
    }
    return render(request, 'user/register.html',context)


def login_user(request):
    query_params = request.GET
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username = request.POST['username'],
                password = request.POST['password']
            )
            if user is not None:
                login(request,user)
                if query_params.get('next'):
                    return redirect(query_params['next'])
                return redirect('/admin')
            print(user)

    context = {
        "form":form
    }
    return render(request, 'user/login.html', context)


