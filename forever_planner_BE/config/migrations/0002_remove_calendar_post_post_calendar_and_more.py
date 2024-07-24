# Generated by Django 5.0.7 on 2024-07-22 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='calendar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='config.calendar'),
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryTitle',
            field=models.CharField(max_length=100),
        ),
    ]
