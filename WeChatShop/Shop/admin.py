from django.contrib import admin
from Shop.models import goods, shopcart, order, consignee, comment, category
from Shop.models import User

# Register your models here.

admin.site.register(goods)
admin.site.register(User)
admin.site.register(shopcart)
admin.site.register(order)
admin.site.register(consignee)
admin.site.register(comment)
admin.site.register(category)