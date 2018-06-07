# Generated by Django 2.0.5 on 2018-06-07 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0027_auto_20180607_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_to_order_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.order_detail'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_to_shopcart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.shopcart'),
        ),
    ]
