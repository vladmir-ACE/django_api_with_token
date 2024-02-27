
from rest_framework import serializers

from .models import Filiere ,Etudiant

class Filiere_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Filiere 
        fields ="__all__"


class Etudiant_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Etudiant 
        fields="__all__"


