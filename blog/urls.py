from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.ArticlesView.as_view(), name='index'),
    path('<int:article_id>', views.ArticleDetailView.as_view(), name='detail'),
]
