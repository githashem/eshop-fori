from django.contrib import admin
from . import models


@admin.register(models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # return True if models.Settings.objects.count() == 0 else False
        return False if models.Settings.objects.exists() else True
