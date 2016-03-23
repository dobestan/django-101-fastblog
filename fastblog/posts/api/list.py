from rest_framework.generics import ListAPIView

from posts.models import Post
from posts.serializers.post import PostListSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
