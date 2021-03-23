from django.contrib import admin
from .models import *

@admin.register(AtcType)
class AtcTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Atc)
class AtcAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
        'author',
        'create_time',
        'update_time'
    )