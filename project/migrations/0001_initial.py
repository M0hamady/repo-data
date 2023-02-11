# Generated by Django 3.2.16 on 2023-01-20 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('finished_at', models.DateTimeField(null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('cost', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('cost', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('start_at', models.DateField(null=True)),
                ('finished_at', models.DateTimeField(null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Moshtarayet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('cost', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.step')),
            ],
        ),
        migrations.CreateModel(
            name='Images_step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=120, null=True)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.step')),
            ],
        ),
    ]