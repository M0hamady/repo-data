# Generated by Django 3.2.16 on 2023-01-22 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_websiteindex_pic_saying_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Montagat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126)),
                ('price', models.FloatField(max_length=126)),
                ('description', models.CharField(max_length=126)),
                ('location', models.CharField(max_length=126)),
                ('qesm', models.CharField(max_length=126)),
            ],
        ),
    ]
