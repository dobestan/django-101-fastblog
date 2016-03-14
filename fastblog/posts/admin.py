from django.contrib import admin

from posts.models import Post, Comment



class PostModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'title',
        'content',

        'is_public',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'is_public',

        'created_at',
        'updated_at',
    )

    search_fields = (
        'title',
        'content',
    )


class CommentModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'content',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'created_at',
        'updated_at',
    )

    search_fields = (
        'content',

        'post__title',
        'post__content',
    )


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
