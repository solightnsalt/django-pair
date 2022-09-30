from django.urls import path
from . import views

app_name = "crud"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("created_at/", views.created_at, name="created_at"),
    path("detail/", views.detail, name="detail"),
]
