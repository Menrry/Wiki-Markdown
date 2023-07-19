from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"), # me permite colocar  cualquier entrada luego de /wiki/ para mostrarla si está en entry ó mostrar Error si no está, también me añadeun formulario con un boton Editar
    path("search/", views.search, name="search"),
    path("new/", views.new_page, name="new_page"),
    path("edit/", views.edit, name="edit"),
    path("save_edit/", views.save_edit, name="save_edit"),
    path("rand/", views.rand, name="rand")
]
