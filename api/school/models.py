from django.db import models

# Create your models here.

class Filiere(models.Model):
    nom=models.CharField(max_length=255)
    code=models.CharField(max_length=200)

    def __str__(self):
        return self.code

class Etudiant(models.Model):
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    age=models.IntegerField()
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom} {self.prenom}"