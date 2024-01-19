# Generated by Django 5.0.1 on 2024-01-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_RPG_Creator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='code',
            field=models.IntegerField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='verified',
            field=models.IntegerField(max_length=1),
        ),
    ]