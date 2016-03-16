from django.views.generic import CreateView

from .base import PostBaseView


class PostCreateView(PostBaseView, CreateView):
    template_name = "posts/new.html"
    fields = [
        'title',
        'content',
    ]
