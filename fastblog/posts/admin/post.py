from django.contrib import admin

from posts.models import Post

from .comment import CommentTabularInline


@admin.register(Post)
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

    inlines = (
        CommentTabularInline,
    )
