# -*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
#
#
#用户
class User(AbstractUser):
    nickname = models.CharField(max_length=150, blank=True)


#订单
class order(models.Model):
    statue = models.CharField(max_length=150, default='待付款')
    order_consignee = models.CharField(max_length=150, default='')#收货人地址
    order_time = models.DateField(auto_now=True)
    order_price = models.FloatField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#订单详情
class order_detail(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)

#购物车
class shopcart(models.Model):
    goods_number = models.IntegerField(blank=True)
    goods_all_price = models.IntegerField(blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#收货人管理
class consignee(models.Model):
    consignee_name = models.CharField(max_length=150)
    consignee_address = models.CharField(max_length=150)
    consignee_phone = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#商品模型
class goods(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=150)
    price = models.FloatField()
    pic_url = models.CharField(max_length=150)
    goods_detail = models.TextField(default='')
    # goods_detail_pic = models.CharField(max_length=150, default='')
    goods_to_shopcart = models.ForeignKey(shopcart, on_delete=models.CASCADE, null=True, blank=True)
    goods_to_order_detail = models.ForeignKey(order_detail, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

# #商品评论模型
# class comment(models.Model):
#     comment_name = models.CharField(max_length=150)
#     comment_content = models.TextField(default='')
#     comment_goods = models.ForeignKey(goods, on_delete=True)
#     comment_time = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.comment_name
# #个人余额
# class records(models.Model):
#     cash = models.FloatField()
#     hongbao = models.FloatField()