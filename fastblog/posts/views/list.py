from django.views.generic import ListView

from .base import PostBaseView


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
