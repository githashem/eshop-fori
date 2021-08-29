from django.db import models
from django.db.models import Q
from eshop_category.models import Category
import os


# upload_image_path
def generate_name_file(instance, file_path):
    name_file = os.path.basename(file_path)
    name, ext = os.path.splitext(name_file)
    return f"products/image/{instance.title}{ext}"


class ProductManager(models.Manager):
    def get_by_id(self, product_id):
        qs = self.filter(id=product_id)
        if qs.exists() and qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, s):
        lookup = (Q(title__icontains=s) |
                  Q(description__icontains=s) |
                  Q(tag__title__icontains=s)
                  )
        return self.filter(lookup, active=True).distinct()

    def get_products_by_category(self, name_category):
        return self.filter(categories__slug__iexact=name_category, active=True)


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    image = models.ImageField(blank=True, null=True, upload_to=generate_name_file, verbose_name="تصویر")
    description = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت")
    active = models.BooleanField(default=False, verbose_name="فعال/غیر فعال بودن")
    categories = models.ManyToManyField(Category)
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')

    objects = ProductManager()

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


# upload_image_path
def generate_name_file_for_gallery(instance, file_path):
    name_file = os.path.basename(file_path)
    name, ext = os.path.splitext(name_file)
    return f"products/galleries/{instance.title}{ext}"


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان", unique=True)
    image = models.ImageField(upload_to=generate_name_file_for_gallery, verbose_name="تصویر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"

