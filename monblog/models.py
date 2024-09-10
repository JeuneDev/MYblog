from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle

class Articles(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    resume = models.TextField(max_length=150)
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles_image/', blank=True, null=True)
    Categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
   
    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    commentaires = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.commentaires
