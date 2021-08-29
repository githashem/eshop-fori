from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from eshop_product.models import Product


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="url")
    active = models.BooleanField(default=False, verbose_name="فعال/غیر فعال بودن")
    time = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ ها"


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        return unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
