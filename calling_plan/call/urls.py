from django.urls import path

from .views import caller

app_name = "call"
urlpatterns = [
    path("caller/", caller, name="caller"),
]
