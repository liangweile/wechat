# -*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
#
#
# 用户
class User(AbstractUser):
    money = models.FloatField(default=0)
    jifen = models.IntegerField(default=0)



# 购物车
class shopcart(models.Model):
    goods_all_price = models.IntegerField(default=0)
    shopcart_id = models.CharField(max_length=150, default='')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


# 收货人管理
class consignee(models.Model):
    consignee_id = models.CharField(max_length=150, default='')
    consignee_sign = models.BooleanField(default=False)
    consignee_name = models.CharField(max_length=150, default='')
    consignee_address = models.CharField(max_length=150, default='')
    consignee_phone = models.CharField(max_length=150, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.consignee_name
# 订单
class order(models.Model):
    pay_method = models.CharField(max_length=159, default='')
    order_id = models.CharField(max_length=150, default='')
    statue = models.CharField(max_length=150, default='待付款')
    order_time = models.DateField(auto_now=True)
    order_price = models.IntegerField(default=0)
    order_price_pay = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_pk = models.ForeignKey(consignee, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user.username


# 订单详情
class order_detail(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)

#商品分类
class category(models.Model):
    category_name = models.CharField(max_length=150)
    def __str__(self):
        return self.category_name


# 商品模型
class goods(models.Model):
    sale = models.IntegerField(default=0)
    title = models.CharField(max_length=150, default='')
    price = models.IntegerField(default=0)
    pic_url = models.CharField(max_length=150, default='')
    pic_url_detail = models.CharField(max_length=150, default='')
    goods_shopcart_number = models.IntegerField(default=0)
    goods_order_number = models.IntegerField(default=0)
    goods_to_shopcart = models.ManyToManyField(shopcart, null=True, blank=True)
    goods_to_order = models.ManyToManyField(order, null=True, blank=True)
    goods_to_user = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True)#收藏
    goods_to_category = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

#商品评论模型
class comment(models.Model):
    comment_name = models.CharField(max_length=150)
    comment_content = models.TextField(default='')
    comment_time = models.DateField(auto_now_add=True)
    comment_level = models.CharField(max_length=150, default="")
    comment_goods = models.ManyToManyField(goods, null=True, blank=True)

    def __str__(self):
        return self.comment_name

