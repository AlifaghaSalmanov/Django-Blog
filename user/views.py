from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
from django.contrib import messages


def register(request):
    form = RegisterForm(request.POST or None)

    context = {
        "form": form,
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        messages.success(request, "Login Succesfully")
        login(request, newUser)

        return redirect("index")

    return render(request, "register.html", context=context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form,
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, "Username or password is incorrect")
            return render(request, "login.html", context)

        messages.success(request, "Login Succesfully")

        login(request, user)

        return redirect("index")
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Succesfully logout")
    return redirect("index")
