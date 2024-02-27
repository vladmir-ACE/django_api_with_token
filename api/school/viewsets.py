from rest_framework import viewsets,generics

from .models import Filiere,Etudiant


from .serializers import Filiere_Serializer,Etudiant_Serializer

class AddFiliere(generics.CreateAPIView):
    serializer_class = Filiere_Serializer

class ListFilieres(generics.ListAPIView):
     queryset=Filiere.objects.all()
     serializer_class=Filiere_Serializer


class UpdateFiliere(generics.UpdateAPIView):
    queryset=Filiere.objects.all()
    serializer_class=Filiere_Serializer
    lookup_field='pk'
    





class AddEtudiant(generics.CreateAPIView):
    
    serializer_class= Etudiant_Serializer


class ListEtudiants(generics.ListAPIView):
    queryset=Etudiant.objects.all()
    serializer_class=Etudiant_Serializer
    
