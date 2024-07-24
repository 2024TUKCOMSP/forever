# Generated by Django 5.0.7 on 2024-07-22 12:29

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_alter_calendar_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='calendar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='config.calendar'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='calendarDate',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='themeId',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]