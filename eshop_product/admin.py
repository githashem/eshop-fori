from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "title", "price", "active"]

    class Meta:
        model = models.Product


@admin.register(models.ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Product, ProductAdmin)
