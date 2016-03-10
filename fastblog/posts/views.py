from django.shortcuts import render

from posts.models import Post


def posts(request):
    context = {
        "posts": Post.objects.all(),
    }

    return render(
        request,
        "posts/list.html",
        context,
    )


def post(request, post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
    }

    return render(
        request,
        "posts/list.html",
        context,
    )
