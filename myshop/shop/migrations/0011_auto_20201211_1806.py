# Generated by Django 2.2.13 on 2020-12-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20201211_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='создан'),
        ),
    ]