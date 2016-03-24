from rest_framework.generics import GenericAPIView

from posts.models import Post


class PostBaseAPIView(GenericAPIView):
    queryset = Post.objects.all()
