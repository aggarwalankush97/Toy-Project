from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('article/', views.article_submit, name='create'),
    path('articles/', views.all_articles, name='articles'),
    path('article-approval', views.article_approval, name='approval'),
    path('articles-edited', views.articles_edited, name='edited'),
    path('article/<int:id>', views.articles_view, name='articles_view'),
    path('approved/<int:id>', views.approved_article, name='approved_view'),
    path('rejected/<int:id>', views.rejected_article, name='rejected_view'),
]
