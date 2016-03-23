from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post


class PostCommentListAPIView(APIView):

    def get(self, request, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))

        data = [
            comment.get_object_dict()
            for comment
            in post.comment_set.all()
        ]

        return Response(data)
