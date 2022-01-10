from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def loginUser(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            error = "Account doesn't exist"
    if not request.user.is_authenticated:
        return render(request, 'login.html', {"error": error})
    else:
        return redirect("/")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/users")
