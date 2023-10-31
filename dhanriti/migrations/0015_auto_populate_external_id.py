# Generated by Django 4.1.4 on 2023-06-07 03:59

from django.db import migrations
import uuid


def generate_unique_external_ids(apps, schema_editor):
    StoryCommentLike = apps.get_model('dhanriti', 'StoryCommentLike')
    StoryRead = apps.get_model('dhanriti', 'StoryRead')

    for row in StoryCommentLike.objects.all():
        row.external_id = uuid.uuid4()
        row.save(update_fields=['external_id'])

    for row in StoryRead.objects.all():
        row.external_id = uuid.uuid4()
        row.save(update_fields=['external_id'])


class Migration(migrations.Migration):

    dependencies = [
        ('dhanriti', '0014_rename_story_part_awarded_part_and_more'),
    ]

    operations = [
        migrations.RunPython(generate_unique_external_ids, reverse_code=migrations.RunPython.noop),
    ]