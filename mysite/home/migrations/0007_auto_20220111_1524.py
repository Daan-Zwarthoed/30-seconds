# Generated by Django 3.1.3 on 2022-01-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220111_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='wordList',
            field=models.JSONField(),
        ),
    ]