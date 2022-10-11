from . import views
from django.urls import path, include

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='home'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('contact/', views.contact, name='contact'),
    path('create/', views.article_create, name='create'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit/<slug:slug>/', views.UpdateArticle.as_view(), name='update'),
    path('delete/<slug:slug>/', views.DeleteArticle.as_view(), name='delete'),
]