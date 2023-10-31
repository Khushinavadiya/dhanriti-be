# Generated by Django 4.1.4 on 2023-04-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dhanriti", "0005_shelf_stories_shelfstorytwo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shelfstory",
            name="shelf",
        ),
        migrations.RemoveField(
            model_name="shelfstory",
            name="story",
        ),
        migrations.AlterField(
            model_name="shelf",
            name="stories",
            field=models.ManyToManyField(
                through="dhanriti.ShelfStoryTwo", to="dhanriti.story"
            ),
        ),
        migrations.DeleteModel(
            name="HistoricalShelfStory",
        ),
        migrations.DeleteModel(
            name="ShelfStory",
        ),
    ]