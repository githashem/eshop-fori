from django.urls import path
from .views import Blog, PostDetail


urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('<int:pk>/', PostDetail.as_view(), name='post'),
]
