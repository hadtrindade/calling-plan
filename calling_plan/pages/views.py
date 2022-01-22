from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="core:login")
def home(request):
    return render(request, "pages/home.html")
