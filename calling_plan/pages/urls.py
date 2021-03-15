from django.urls import path
from calling_plan.pages.views import home

app_name = "pages"

urlpatterns = [
    path("", home, name="home"),
]
