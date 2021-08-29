from django.contrib import admin
from . import models


class TagAdmin(admin.ModelAdmin):

    class Meta:
        model = models.Tag


admin.site.register(models.Tag, TagAdmin)
