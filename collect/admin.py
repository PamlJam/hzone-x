from django.contrib import admin
from .models import Collection

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'content_object',
        'object_id',
        'user',
    )