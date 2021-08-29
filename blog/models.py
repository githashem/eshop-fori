from django.db import models
import os


# upload_image_path
def generate_name_file(instance, file_path):
    name_file = os.path.basename(file_path)
    name, ext = os.path.splitext(name_file)
    return f"posts/image/{instance.title}{ext}"


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    image = models.ImageField(blank=True, null=True, upload_to=generate_name_file, verbose_name="تصویر")
    description = models.TextField(verbose_name="توضیحات")
    is_publish = models.BooleanField(default=False, verbose_name="انتشار/پیشنویس")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "خبرها"
