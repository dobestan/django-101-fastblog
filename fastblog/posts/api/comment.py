from rest_framework.generics import ListAPIView

from posts.models import Post
from posts.serializers.comment import CommentListSerializer


class PostCommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        return post.comment_set.all()
