# Generated by Django 2.0.5 on 2018-06-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20180529_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='pic_url',
            field=models.CharField(max_length=150),
        ),
    ]
