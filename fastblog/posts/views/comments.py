from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post, Comment


class PostCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = [
        'content',
    ]

    def form_valid(self, form):
        # User
        form.instance.user = self.request.user

        # Post
        form.instance.post = Post.objects.get(
            pk=self.kwargs.get('pk'),
        )

        return super(PostCommentCreateView, self).form_valid(form)
