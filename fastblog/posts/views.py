from django.views.generic import View, ListView, DetailView, CreateView
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from posts.models import Post


class PostBaseView(View):
    model = Post


# class PostListView(PostBaseView, ListView):
#     template_name = "posts/list.html"
#     context_object_name = "posts"

def posts(request):
    page = request.GET.get('page', 1)
    posts_per_page = request.GET.get('per', 3)

    paginator = Paginator(
        Post.objects.all(),
        posts_per_page,
    )
    posts = paginator.page(page)

    return render(
        request,
        "posts/list.html",
        context={
            'posts': posts,
        }
    )


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
