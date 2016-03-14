from django.views.generic import View, ListView, DetailView, CreateView
from django.shortcuts import redirect, render

from posts.models import Post


class PostBaseView(View):
    model = Post


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"


class PostDetailView(PostBaseView, DetailView):
    template_name = "posts/detail.html"


def post_comments(request, pk):
    post = Post.objects.get(pk=pk)
    comment = post.comment_set.create(
        content=request.POST.get("content"),
    )

    return redirect(post)


class PostCreateView(PostBaseView, CreateView):
    template_name = "posts/new.html"
    fields = [
        'title',
        'content',
    ]
