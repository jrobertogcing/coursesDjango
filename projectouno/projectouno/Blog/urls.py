from django.urls import path, include

from .views import ArticleListView

app_name = 'articles'

urlpatterns = [
    
    path('Blog', ArticleListView.as_view(), name = "article-list"),

]