# Generated by Django 2.0.5 on 2018-06-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_consignee_consignee_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consignee',
            name='consignee_sign',
            field=models.BooleanField(default=False),
        ),
    ]
