# Generated by Django 2.0.5 on 2018-06-03 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0021_shopcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_to_shopcart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Shop.shopcart'),
        ),
    ]
