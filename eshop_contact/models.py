from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="اسم کامل")
    email = models.EmailField(max_length=100, verbose_name="ایمیل")
    subject = models.CharField(max_length=200, verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده/نشده")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "تماس"
        verbose_name_plural = "تماس ها"
