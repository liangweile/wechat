from django.contrib import admin
from Shop.models import goods, shopcart, order, order_detail, consignee
from Shop.models import User

# Register your models here.

admin.site.register(goods)
admin.site.register(User)
admin.site.register(shopcart)
admin.site.register(order)
admin.site.register(order_detail)
admin.site.register(consignee)