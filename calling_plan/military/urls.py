from django.urls import path
from .views import (
    AreaCreate,
    MilitaryCreate,
    SubUnitCreate,
    GraduationCreate,
    list_military,
    details_military,
    edit_military,
    delete_military,
    list_subunit,
    list_graduation,
    list_area,
)

app_name = "military"

urlpatterns = [
    path("add-area/", AreaCreate.as_view(), name="add-area"),
    path("add-military/", MilitaryCreate.as_view(), name="add-military"),
    path("add-subunit/", SubUnitCreate.as_view(), name="add-subunit"),
    path(
        "add-graduation/",
        GraduationCreate.as_view(),
        name="add-graduation",
    ),
    path("list-military/", list_military, name="list-military"),
    path("list-subunit/", list_subunit, name="list-subunit"),
    path("list-graduation/", list_graduation, name="list-graduation"),
    path("list-area/", list_area, name="list-area"),
    path("details-military/<str:pk>/", details_military, name="details-military"),
    path("edit-military/<str:pk>/", edit_military, name="edit-military"),
    path("delete-military/<str:pk>/", delete_military, name="delete-military"),
]
