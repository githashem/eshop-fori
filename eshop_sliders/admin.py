from django.contrib import admin
from . import models


@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    pass
