from . import views
from django.urls import path
from .feeds import LatestPostsFeed

urlpatterns = [
    #path('', views.PostLists.as_view(), name='home'), 
    path('', views.PostLists, name='home'),   
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]