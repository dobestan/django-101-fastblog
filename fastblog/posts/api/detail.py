from rest_framework.generics import RetrieveAPIView

from posts.models import Post
from posts.serializers.post import PostDetailSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
