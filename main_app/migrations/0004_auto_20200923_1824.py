# Generated by Django 3.1.1 on 2020-09-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=True),
        ),
    ]