# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_category_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
