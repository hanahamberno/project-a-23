from django.contrib import admin
from django.contrib.auth.models import User
from . import models

# Register your models here.
@admin.register(models.Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'sender',
        'recipient',
        'body',
        'date',
        'is_read',
    )