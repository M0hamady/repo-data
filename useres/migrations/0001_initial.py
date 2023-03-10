# Generated by Django 3.2.16 on 2022-12-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('ip', models.CharField(max_length=120, null=True)),
                ('info', models.CharField(max_length=120, null=True)),
                ('phone', models.CharField(max_length=120, null=True)),
                ('location', models.CharField(max_length=120, null=True)),
                ('is_visitor', models.BooleanField(default=True)),
                ('is_client', models.BooleanField(default=True)),
                ('is_eng', models.BooleanField(default=True)),
                ('is_designer', models.BooleanField(default=True)),
                ('is_manager', models.BooleanField(default=True)),
            ],
        ),
    ]
