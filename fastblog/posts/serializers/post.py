from rest_framework import serializers

from posts.models import Post
from .comment import CommentListSerializer


class PostBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )


class PostListSerializer(PostBaseSerializer):
    pass


class PostDetailSerializer(PostBaseSerializer):

    # comment_set = CommentListSerializer(many=True)
    comments = CommentListSerializer(many=True)

    class Meta(PostBaseSerializer.Meta):
        fields = PostBaseSerializer.Meta.fields + (
            'comments',
        )
