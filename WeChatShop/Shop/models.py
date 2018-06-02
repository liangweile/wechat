from django.db import models

# Create your models here.

class goods(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=150)
    price = models.FloatField()
    pic_url = models.FilePathField(path="/home/xiaojun/PycharmProjects/weixin/WeChatShop/Shop/static/images")

    def __str__(self):
        return self.title