from rest_framework import serializers

from posts.models import Comment


class CommentBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'content',
        )


class CommentListSerializer(CommentBaseSerializer):
    pass
