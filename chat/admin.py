from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ('owner', 'created')
    list_display = ('text', 'to_chat')
    search_fields = ('owner', 'to_chat')


@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    pass
