# Generated by Django 5.1.1 on 2024-12-21 14:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e0cd5387-64d0-4e80-b7dc-c70541a6b0d1'), editable=False, primary_key=True, serialize=False),
        ),
    ]
