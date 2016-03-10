from django.shortcuts import render

from posts.models import Post


def posts(request):

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        post = Post.objects.create(
            title=title,
            content=content,
        )

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
        "posts/detail.html",
        context,
    )
