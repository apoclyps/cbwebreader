# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-31 10:40
from __future__ import unicode_literals

from django.db import migrations, models

import uuid


class Migration(migrations.Migration):

    dependencies = [("comic", "0009_auto_20160331_1140")]

    operations = [
        migrations.AlterField(
            model_name="comicbook", name="selector", field=models.UUIDField(default=uuid.uuid4, unique=True)
        ),
        migrations.AlterField(
            model_name="directory", name="selector", field=models.UUIDField(default=uuid.uuid4, unique=True)
        ),
    ]
