from django.views.generic import View

from django.http import HttpResponse

import json

from posts.models import Post


class PostListAPIView(View):

    def get(self, request):

        posts = Post.objects.all()
        data = [
            post.get_object_dict()
            for post
            in posts
        ]

        return HttpResponse(
            json.dumps(data),
            content_type="application/json",
        )
