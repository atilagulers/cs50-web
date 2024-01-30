from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random, name="random"),
    path("wiki/create", views.create, name="create"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, 
    name="entry"),
    path("error", views.error, name="error"),
]
