from django.contrib import admin
from .models import *

@admin.register(Item)
class AtcTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'sold',
        'info',
        'time',
        'chop',
        'link',
        'owner',
        'price',
        'count',
    )