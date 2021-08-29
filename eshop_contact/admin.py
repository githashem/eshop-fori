from django.contrib import admin
from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email", "is_read"]
    list_filter = ["is_read"]
    list_editable = ["is_read"]
    search_fields = ["subject", "message"]
