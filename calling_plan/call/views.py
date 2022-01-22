from django.shortcuts import render

# Create your views here.


def caller(request):
    context = {"form": "teste"}
    return render(request, "registration/register.html", context=context)
