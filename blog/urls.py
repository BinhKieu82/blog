from . import views
from django.urls import path, include

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='home'),
    path('create/', views.article_create, name='create'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit/<slug:slug>/', views.UpdateArticle.as_view(), name='update'),
]