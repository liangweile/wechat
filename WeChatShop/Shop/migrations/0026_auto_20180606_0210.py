# Generated by Django 2.0.5 on 2018-06-06 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0025_auto_20180606_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='statue',
            field=models.CharField(default='待付款', max_length=150),
        ),
    ]
