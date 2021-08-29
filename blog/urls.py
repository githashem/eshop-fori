from django.urls import path
from .views import Blog, PostDetail, SearchPostListView


urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('<int:pk>/', PostDetail.as_view(), name='post'),
    path('post/search/', SearchPostListView.as_view(), name='search_post'),
]
