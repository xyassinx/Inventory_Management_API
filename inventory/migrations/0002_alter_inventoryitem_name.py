# Generated by Django 5.1.4 on 2025-01-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
