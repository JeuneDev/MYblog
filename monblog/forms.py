from django import forms
from .models import Articles, Commentaire
from .models import Categorie

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['libelle']
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la catégorie'}),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['titre', 'contenu', 'resume', 'image', 'Categorie']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'article'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Contenu de l\'article'}),
            'resume': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Résumé'}),
            'Categorie': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['commentaires']
        widgets = {
            'commentaires': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Votre commentaire'}),
        }
