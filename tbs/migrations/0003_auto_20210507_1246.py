# Generated by Django 3.1.7 on 2021-05-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbs', '0002_auto_20210507_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='mob_number',
            field=models.CharField(max_length=10),
        ),
    ]
