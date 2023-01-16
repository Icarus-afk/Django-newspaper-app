from django.urls import path
from .views import ArticleListView


urlspatterns = [
    path('', ArticleListView.as_view(), name = 'article_list')
]