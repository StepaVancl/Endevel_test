# Generated by Django 4.1 on 2022-09-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="picture_url",
            field=models.URLField(blank=True, max_length=256),
        ),
    ]
