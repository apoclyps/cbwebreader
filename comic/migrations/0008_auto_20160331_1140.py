# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-31 10:40
from __future__ import unicode_literals

import datetime
import uuid

import django.db.models.deletion
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("comic", "0007_auto_20150626_1820")]

    operations = [
        migrations.CreateModel(
            name="Directory",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("selector", models.UUIDField(default=uuid.uuid4, null=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="comic.Directory"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="comicbook",
            name="date_added",
            field=models.DateTimeField(
                auto_now_add=True, default=datetime.datetime(2016, 3, 31, 10, 40, 30, 62170, tzinfo=utc)
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="comicbook", name="selector", field=models.UUIDField(default=uuid.uuid4, null=True)
        ),
        migrations.AddField(model_name="comicbook", name="version", field=models.IntegerField(default=0)),
        migrations.AddField(
            model_name="comicbook",
            name="directory",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="comic.Directory"
            ),
        ),
    ]
