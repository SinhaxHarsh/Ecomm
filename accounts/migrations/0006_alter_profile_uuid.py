# Generated by Django 5.1.1 on 2024-12-23 07:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b04cd282-b680-4588-b7be-0baf7af9ef48'), editable=False, primary_key=True, serialize=False),
        ),
    ]
