# Generated by Django 2.0.6 on 2018-06-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0035_auto_20180622_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='pic_url_detail',
            field=models.CharField(default='', max_length=150),
        ),
    ]
