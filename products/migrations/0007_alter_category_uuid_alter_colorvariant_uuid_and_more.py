# Generated by Django 5.1.1 on 2024-12-22 10:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_color_vaiant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('97e6020f-ada1-48a2-997f-9d781833de44'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='colorvariant',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('97e6020f-ada1-48a2-997f-9d781833de44'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('97e6020f-ada1-48a2-997f-9d781833de44'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('97e6020f-ada1-48a2-997f-9d781833de44'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sizevariant',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('97e6020f-ada1-48a2-997f-9d781833de44'), editable=False, primary_key=True, serialize=False),
        ),
    ]
