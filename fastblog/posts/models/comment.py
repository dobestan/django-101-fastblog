from django.db import models
from django.core.urlresolvers import reverse


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

    def get_absolute_url(self):
        return "{post_url}{comment_tag_id}".format(
            post_url = reverse(
                "post",
                kwargs={
                    "pk": self.id,
                }
            ),
            comment_tag_id = "#comment_{comment_id}".format(
                comment_id=self.id,
            ),
        )
