# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-01 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [("comic", "0011_auto_20160331_1141")]

    operations = [
        migrations.AlterField(
            model_name="comicbook",
            name="selector",
            field=models.UUIDField(db_index=True, default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name="directory",
            name="selector",
            field=models.UUIDField(db_index=True, default=uuid.uuid4, unique=True),
        ),
    ]
