# -*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
#
#
# 用户
class User(AbstractUser):
    nickname = models.CharField(max_length=150, blank=True)



# 购物车
class shopcart(models.Model):
    goods_all_price = models.IntegerField(default=0)
    shopcart_id = models.CharField(max_length=150, default='')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


# 收货人管理
class consignee(models.Model):
    consignee_sign = models.BooleanField(default=False)
    consignee_name = models.CharField(max_length=150, default='')
    consignee_address = models.CharField(max_length=150, default='')
    consignee_phone = models.CharField(max_length=150, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
# 订单
class order(models.Model):
    statue = models.CharField(max_length=150, default='待付款')
    order_sign = models.BooleanField(default=False)
    order_time = models.DateField(auto_now=True)
    order_price = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_pk = models.ForeignKey(consignee, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


# 订单详情
class order_detail(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)

# 商品模型
class goods(models.Model):
    title = models.CharField(max_length=150, default='')
    desc = models.CharField(max_length=150, default='')
    price = models.IntegerField(default=0)
    pic_url = models.CharField(max_length=150, default='')
    goods_detail = models.TextField(default='')
    # goods_detail_pic = models.CharField(max_length=150, default='')
    goods_shopcart_number = models.IntegerField(default=0)
    goods_to_shopcart = models.ForeignKey(shopcart, on_delete=models.CASCADE, null=True, blank=True)
    goods_to_order = models.ManyToManyField(order, null=True, blank=True)

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
