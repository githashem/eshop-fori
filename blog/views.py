from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class Blog(ListView):
    model = Post
    paginate_by = 3
    queryset = Post.objects.all().filter(is_publish=True)


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    queryset = Post.objects.all().filter(is_publish=True)
