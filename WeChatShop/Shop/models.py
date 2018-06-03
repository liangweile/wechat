from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#
#
#用户
class User(AbstractUser):
    nickname = models.CharField(max_length=150, blank=True)


#订单
class order(models.Model):
    statue = models.IntegerField(default=-1)#-1待支付 0待收货 1待评价
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    add = models.CharField(max_length=150, default='')

#购物车
class shopcart(models.Model):
    goods_number = models.IntegerField(default=0)
    goods_all_price = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)



#商品模型
class goods(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=150)
    price = models.FloatField()
    # pic_url = models.FilePathField(path="/static/images")
    pic_url = models.CharField(max_length=150)
    # goods_detail = models.TextField(default='')
    # goods_detail_pic = models.CharField(max_length=150, default='')
    goods_to_shopcart = models.ForeignKey(shopcart, on_delete=models.CASCADE, default='')
    goods_to_order = models.ForeignKey(order, on_delete=models.CASCADE, default='')

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