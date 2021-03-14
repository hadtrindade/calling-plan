from django.urls import path
from .views import (
    AreaCreate,
    MilitaryCreate,
    SubUnidadeCreate,
    PostoGraduacaoCreate,
    list_military,
    details_military,
    list_subunit,
    list_graduation,
    list_area,
)

app_name = "military"

urlpatterns = [
    path("add-area/", AreaCreate.as_view(), name="add-area"),
    path("add-military/", MilitaryCreate.as_view(), name="add-military"),
    path("add-subunit/", SubUnidadeCreate.as_view(), name="add-subunit"),
    path(
        "add-graduation/",
        PostoGraduacaoCreate.as_view(),
        name="add-graduation",
    ),
    path("list-military/", list_military, name="list-military"),
    path("list-subunit/", list_subunit, name="list-subunit"),
    path("list-graduation/", list_graduation, name="list-graduation"),
    path("list-area/", list_area, name="list-area"),
    path("details-military/<str:pk>/", details_military, name="details-military"),
]
