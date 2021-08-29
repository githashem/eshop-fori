from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from eshop_settings.models import Settings


class Blog(ListView):
    model = Post
    paginate_by = 3
    queryset = Post.objects.all().filter(is_publish=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['options'] = Settings.object()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    queryset = Post.objects.all().filter(is_publish=True)


class SearchPostListView(ListView):
    template_name = 'blog/post_list.html'
    paginate_by = 3

    def get_queryset(self):
        s = self.request.GET.get("s")
        if s is not None:
            return Post.objects.search(s)
        return Post.objects.filter(is_publish=True)
