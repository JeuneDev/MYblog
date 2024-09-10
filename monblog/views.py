from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Articles, Commentaire, Categorie
from .forms import ArticleForm, CommentaireForm
from .forms import CategorieForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Liste des articles de l'utilisateur connecté
class UserArticlesListView(LoginRequiredMixin, ListView):
    model = Articles
    template_name = 'monblog/user_article.html'
    context_object_name = 'articles'
    
    def get_queryset(self):
        # Retourne uniquement les articles de l'utilisateur connecté
        return Articles.objects.filter(auteur=self.request.user)

# Vue pour la modification d'un article
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ['titre', 'contenu', 'resume', 'image', 'Categorie']
    template_name = 'monblog/edit_article.html'
    
    def form_valid(self, form):
        form.instance.auteur = self.request.user  # L'utilisateur connecté est l'auteur
        return super().form_valid(form)
    
    def test_func(self):
        # Vérifie si l'utilisateur connecté est l'auteur de l'article
        article = self.get_object()
        return self.request.user == article.auteur

# Vue pour la suppression d'un article
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    success_url = reverse_lazy('articles:user_articles')  # Redirige vers la liste des articles de l'utilisateur
    template_name = 'monblog/delete_article.html'
    
    def test_func(self):
        # Vérifie si l'utilisateur connecté est l'auteur de l'article
        article = self.get_object()
        return self.request.user == article.auteur

class HomePageView(ListView):
    model = Articles
    template_name = 'monblog/home.html'
    context_object_name = 'articles'
    paginate_by = 10  # Ajustez selon vos besoins

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Récupérer le dernier article globalement
        latest_article = Articles.objects.latest('date_publication')
        # Compter le nombre de commentaires pour ce dernier article
        latest_article_comment_count = Commentaire.objects.filter(article=latest_article).count()
        
        # Ajouter ces informations au contexte
        context['latest_article'] = latest_article
        context['latest_article_comment_count'] = latest_article_comment_count
        
        # Récupérer toutes les catégories
        context['categories'] = Categorie.objects.all()
        
        return context

class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'monblog/creer_categorie.html'
    success_url = reverse_lazy('articles:liste_categories')

class CategorieListView(ListView):
    model = Categorie
    template_name = 'monblog/liste_categorie.html'
    context_object_name = 'categories'

# views.py de l'application articles

class ArticlesParCategorieView(ListView):
    model = Articles
    template_name = 'monblog/articles_par_categorie.html'
    context_object_name = 'articles'

    def get_queryset(self):
        self.categorie = get_object_or_404(Categorie, pk=self.kwargs['pk'])
        return Articles.objects.filter(Categorie=self.categorie)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorie'] = self.categorie
        return context


def article_list(request):
    articles = Articles.objects.all()
    return render(request, 'monblog/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    commentaires = article.commentaire_set.all()
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.auteur = request.user
            commentaire.save()
            return redirect('articles:detail_article', article_id=article_id)
    else:
        form = CommentaireForm()
    return render(request, 'monblog/article_detail.html', {'article': article, 'commentaires': commentaires, 'form': form})

@login_required
def creer_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.save()
            return redirect('articles:article_list')
    else:
        form = ArticleForm()
    return render(request, 'monblog/article_form.html', {'form': form})

# Create your views here.
