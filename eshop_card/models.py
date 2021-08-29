from django.db import models
from django.contrib.auth.models import User
from eshop_product.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    payment_date = models.DateTimeField(verbose_name="تاریخ پرداخت", null=True, blank=True)
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده/نشده")
    trcking_code = models.CharField(max_length=30, verbose_name='کد رهگیری', null=True, blank=True)

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش ها"

    def __str__(self):
        return self.owner.get_full_name()

    def get_total(self):
        return sum([detail.count * detail.price for detail in self.orderdetail_set.all()])


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    price = models.IntegerField(verbose_name="قیمت")
    count = models.IntegerField(verbose_name="تعداد")

    class Meta:
        verbose_name = "جزییات سفارش"
        verbose_name_plural = "جزییات سفارش ها"

    def __str__(self):
        return self.product.title

    def get_total(self):
        return self.count * self.price
