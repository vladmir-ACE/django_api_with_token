from django.urls import path
from .viewsets import AddFiliere,AddEtudiant,ListFilieres,ListEtudiants,UpdateFiliere
urlpatterns=[
    path("addFiliere/",AddFiliere.as_view(), name="addFiliere"),
    path("listFiliere/",ListFilieres.as_view(), name="listFiliere"),
    path("updateFiliere/<int:pk>/",UpdateFiliere.as_view(), name="updateFiliere"),

    path("addEtudiant/",AddEtudiant.as_view(), name="addEtudiant"),
    path("listEtudiant/",ListEtudiants.as_view(), name="listEtudiant")
    


]