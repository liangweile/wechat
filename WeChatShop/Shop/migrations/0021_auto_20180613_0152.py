# Generated by Django 2.0.5 on 2018-06-13 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0020_auto_20180612_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='consignee',
            name='consignee_id',
            field=models.CharField(default='', max_length=150),
        ),
    ]
