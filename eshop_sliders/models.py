from django.db import models
import os


# upload_image_path
def generate_name_file(instance, file_path):
    name_file = os.path.basename(file_path)
    name, ext = os.path.splitext(name_file)
    return f"sliders/image/{instance.title}{ext}"


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    link = models.URLField(max_length=100, verbose_name="لینک")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(blank=True, null=True, upload_to=generate_name_file, verbose_name="تصویر")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدرها"
