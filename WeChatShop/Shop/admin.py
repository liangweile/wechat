from django.contrib import admin
from Shop.models import goods

# Register your models here.

class goods_admin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'pic_url']

admin.site.register(goods, goods_admin)