# Generated by Django 3.1.7 on 2021-05-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbs', '0004_auto_20210507_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='book_time',
        ),
        migrations.AlterField(
            model_name='table',
            name='mob_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='person_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]