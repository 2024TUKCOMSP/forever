# Generated by Django 5.0.7 on 2024-07-25 14:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_alter_category_categorycolor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('themeId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('themeTitle', models.CharField(max_length=255)),
                ('colorList', models.JSONField()),
            ],
        ),
    ]
