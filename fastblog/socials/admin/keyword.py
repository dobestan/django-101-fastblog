from django.contrib import admin

from socials.models import Keyword


@admin.register(Keyword)
class KeywordModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'name',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'created_at',
        'updated_at',
    )

    search_fields = (
        'name',
    )

    inlines = (
    )
