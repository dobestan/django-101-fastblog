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
