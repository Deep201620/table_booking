# Generated by Django 3.1.7 on 2021-05-11 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbs', '0007_auto_20210507_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='members',
            field=models.CharField(default=0, max_length=2),
        ),
    ]