from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from calling_plan.decorators import allowed_users, unauthenticated_user

from .forms import UserCreationForm


@unauthenticated_user
def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("pages:home")
        else:
            messages.error(request, "Usuário ou senha inváidos.")

    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("core:login")


@login_required(login_url="core:login")
@allowed_users(allowed_roles=["admin"])
def register_view(request):

    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pages:home")
        else:
            messages.error(request, "As senhas não conferem.")
    context = {"form": form}
    return render(request, "registration/register.html", context=context)
