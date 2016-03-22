from django.contrib import admin

from socials.models import SocialPost


@admin.register(SocialPost)
class SocialPostModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'keyword',
        'title',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'keyword',

        'created_at',
        'updated_at',
    )

    search_fields = (
        'title',
    )

    inlines = (
    )
