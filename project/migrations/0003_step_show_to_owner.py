# Generated by Django 3.2.16 on 2023-01-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20230120_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='show_to_owner',
            field=models.BooleanField(default=False),
        ),
    ]
