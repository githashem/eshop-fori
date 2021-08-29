from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = models.Category


admin.site.register(models.Category, CategoryAdmin)
