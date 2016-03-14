from django.views.generic import View, ListView, DetailView
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


def new_post(request):

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(
            title=title,
            content=content,
        )

        return redirect(post)

    return render(
        request,
        "posts/new.html",
        context={}
    )
