# Generated by Django 2.0.5 on 2018-06-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_auto_20180603_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='statue',
            field=models.IntegerField(default=-1),
        ),
    ]