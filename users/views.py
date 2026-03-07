from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def auth_route(request):
    return render(request, 'users/auth.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('profiles:profile')        
        return redirect('users:register')
    return render(request, 'users/register.html', {'reg_form': UserCreationForm()})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profiles:profile')
        return redirect('users:login')
    return render(request, 'users/login.html', {'login_form': AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('users:login')
