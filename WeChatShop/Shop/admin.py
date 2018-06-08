from django.contrib import admin
from Shop.models import goods, shopcart, order, order_detail, consignee
from Shop.models import User

# Register your models here.

class goods_admin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'pic_url']


class order_admin(admin.ModelAdmin):
    list_display = ['statue']


admin.site.register(goods, goods_admin)
admin.site.register(User)
admin.site.register(shopcart)
admin.site.register(order, order_admin)
admin.site.register(order_detail)
admin.site.register(consignee)