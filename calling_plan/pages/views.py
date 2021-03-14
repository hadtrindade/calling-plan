from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="core:login")
def home(request):
    return render(request, "pages/home.html")
