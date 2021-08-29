from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(blank=True, verbose_name="عنوان در url")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

