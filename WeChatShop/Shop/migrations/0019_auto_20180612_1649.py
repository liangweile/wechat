# Generated by Django 2.0.5 on 2018-06-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0018_auto_20180612_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='statue',
            field=models.CharField(default='代付款', max_length=150),
        ),
    ]
