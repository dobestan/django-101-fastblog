from rest_framework import serializers

from posts.models import Post


class PostBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )
