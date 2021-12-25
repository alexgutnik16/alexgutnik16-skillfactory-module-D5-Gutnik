from django.urls import path
from .views import News, NewsDetailView, Search, PostCreateView, NewsUpdateView, NewsDeleteView, upgrade_me


urlpatterns = [
    path('', News.as_view()),
    path('<int:pk>', NewsDetailView.as_view(), name='post'),
    path('search/', Search.as_view()),
    path('add/', PostCreateView.as_view()),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='post_delete'),
    path('upgrade/', upgrade_me, name='upgrade')
]
