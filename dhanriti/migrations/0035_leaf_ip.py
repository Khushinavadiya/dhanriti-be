# Generated by Django 4.2.2 on 2023-08-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dhanriti", "0034_alter_part_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="leaf",
            name="ip",
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]