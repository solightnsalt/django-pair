from django.urls import path
from . import views

app_name = "crud"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("created_at/", views.created_at, name="created_at"),
    path("detail/<int:review_pk>", views.detail, name="detail"),
    path("delete/<int:review_pk>", views.delete, name="delete"),
    path("update/<int:review_pk>", views.update, name="update"),
    path("updated/<int:review_pk>", views.updated, name="updated"),    
]
