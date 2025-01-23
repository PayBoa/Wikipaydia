from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entrytitle>", views.entrycontent, name="entrycontent"),
    path("searchresults", views.searchresults, name="searchresults" )
]
