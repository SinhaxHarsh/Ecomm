# Generated by Django 5.1.1 on 2024-12-22 07:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1c2afa6e-5fc5-4def-922e-694f30b66082'), editable=False, primary_key=True, serialize=False),
        ),
    ]
