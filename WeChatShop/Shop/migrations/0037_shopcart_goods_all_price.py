# Generated by Django 2.0.5 on 2018-06-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0036_auto_20180608_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='goods_all_price',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
