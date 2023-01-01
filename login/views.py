from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:

            messages.success(request, ("there was an error"))
            return redirect('login')
    else:
        return render(request, 'login/login.html', {})

def logut_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registr succes"))
            return redirect('/')
        else:
            print(form.errors)

    else:
        form = UserCreationForm()

    return render(request, 'login/registartion.html')