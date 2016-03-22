from django.contrib import admin

from communications.models import SMS, Email, Slack


@admin.register(SMS)
@admin.register(Email)
@admin.register(Slack)
class MessageModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'receiver',
        'sender',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'created_at',
        'updated_at',
    )

    search_fields = (
        'content',
    )
