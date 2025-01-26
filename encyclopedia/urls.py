from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("searchresults/", views.searchresults, name="searchresults" ),
    path("newpage", views.newpage, name="newpage" ),
    path("editpage", views.editpage, name="editpage"),
    path("<str:entrytitle>", views.entrycontent, name="entrycontent"),
]
