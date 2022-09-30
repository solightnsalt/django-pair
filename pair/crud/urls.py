from django.urls import path
from . import views

app_name = "crud"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("detail/<pk>", views.detail, name="detail"),
]
