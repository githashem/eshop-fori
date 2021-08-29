from django.db import models


class Settings(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=150)
    phone = models.CharField(verbose_name="تلفن", max_length=50)
    mobile = models.CharField(verbose_name="موبایل", max_length=50)
    email = models.EmailField(verbose_name="ایمیل", max_length=100)
    address = models.CharField(verbose_name="آدرس", max_length=250)
    copy_right = models.CharField(verbose_name="کپی رایت", max_length=200)
    about = models.TextField(verbose_name="درباره")
    logo = models.ImageField(verbose_name="لوگو", upload_to="logo", blank=True, null=True)

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "مدیریت تنظیمات"

    def __str__(self):
        return self.title

    @classmethod
    def object(cls):
        return cls._default_manager.all().first()

    def save(self, *args, **kwargs):
        self.id = 1  # self.pk = self.id = 1
        return super(Settings, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if not self.pk and Settings.objects.exists():
    #         raise ValidationError("There is can be only one Settings instance")
    #     return super(Settings, self).save(*args, **kwargs)
