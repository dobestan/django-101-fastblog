from rest_framework.generics import ListAPIView

from posts.serializers.post import PostListSerializer
from .base import PostBaseAPIView


class PostListAPIView(PostBaseAPIView, ListAPIView):
    serializer_class = PostListSerializer
