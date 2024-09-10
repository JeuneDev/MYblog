from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('article_list', views.article_list, name='article_list'),  # Page principale avec la liste des articles
    path('article/<int:article_id>/', views.article_detail, name='detail_article'),  # Détail d'un article avec commentaires
    path('article/nouveau/', views.creer_article, name='creer_article'),  # Création d'un nouvel article
    path('categorie/creer/', views.CategorieCreateView.as_view(), name='creer_categorie'),
    path('categories/', views.CategorieListView.as_view(), name='liste_categories'),
    path('categorie/<int:pk>/', views.ArticlesParCategorieView.as_view(), name='articles_par_categorie'),
     path('mes-articles/', views.UserArticlesListView.as_view(), name='user_articles'),
    path('article/<int:pk>/modifier/', views.ArticleUpdateView.as_view(), name='edit_article'),
    path('article/<int:pk>/supprimer/', views.ArticleDeleteView.as_view(), name='delete_article'),
    # Ajoutez d'autres URLs pour modifier ou supprimer des articles si nécessaire
]
