# Generated by Django 3.1.3 on 2022-01-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='wordList',
            field=models.TextField(default=[]),
            preserve_default=False,
        ),
    ]