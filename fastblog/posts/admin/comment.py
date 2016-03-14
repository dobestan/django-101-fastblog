from django.contrib import admin

from posts.models import Comment


@admin.register(Comment)
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


class CommentTabularInline(admin.TabularInline):

    model = Comment
