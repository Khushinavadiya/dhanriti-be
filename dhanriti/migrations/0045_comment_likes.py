# Generated by Django 4.2.5 on 2023-09-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dhanriti", "0044_email_sent_email_subject"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]