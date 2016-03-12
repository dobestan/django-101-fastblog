from django.db import models


class Comment(models.Model):
    post = models.ForeignKey("Post")
    content = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return 'Commented "{comment_content}" on "{post_title}"'.format(
            comment_content=self.content,
            post_title=self.post.title,
        )
