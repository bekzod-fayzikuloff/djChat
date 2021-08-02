from django.contrib import admin
from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MessagePrivate)
class MessagePrivateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MessageReference)
class MessageReferenceAdmin(admin.ModelAdmin):
    pass