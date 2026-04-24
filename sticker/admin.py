from django.contrib import admin
from .models import StickerRecord, GoalSetting


@admin.register(StickerRecord)
class StickerRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'cast_name', 'count')
    list_filter = ('date', 'cast_name')
    ordering = ('-date', '-id')


@admin.register(GoalSetting)
class GoalSettingAdmin(admin.ModelAdmin):
    pass
