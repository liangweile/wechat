# Generated by Django 2.0.5 on 2018-06-13 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0025_auto_20180613_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pay_method',
        ),
    ]