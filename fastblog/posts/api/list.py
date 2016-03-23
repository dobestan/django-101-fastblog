from rest_framework.views import APIView
from rest_framework.response import Response


from posts.models import Post


class PostListAPIView(APIView):

    def get(self, request):

        posts = Post.objects.all()
        data = [
            post.get_object_dict()
            for post
            in posts
        ]

        return Response(data)
