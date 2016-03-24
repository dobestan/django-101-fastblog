from rest_framework.generics import RetrieveAPIView

from posts.serializers.post import PostDetailSerializer
from .base import PostBaseAPIView


class PostDetailAPIView(PostBaseAPIView, RetrieveAPIView):
    serializer_class = PostDetailSerializer
