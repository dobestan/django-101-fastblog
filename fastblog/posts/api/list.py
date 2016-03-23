from rest_framework.generics import ListAPIView

from posts.models import Post
from posts.serializers.post import PostBaseSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostBaseSerializer
