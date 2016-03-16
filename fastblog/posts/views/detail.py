from django.views.generic import DetailView

from .base import PostBaseView


class PostDetailView(PostBaseView, DetailView):
    template_name = "posts/detail.html"
