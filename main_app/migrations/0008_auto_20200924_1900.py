# Generated by Django 3.1.1 on 2020-09-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200924_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pill',
            name='doses_taken',
        ),
        migrations.AddField(
            model_name='pill',
            name='doses_left',
            field=models.IntegerField(default=3),
        ),
    ]
