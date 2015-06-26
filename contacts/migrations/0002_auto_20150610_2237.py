# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.IntegerField(null=True, choices=[(1, b'Male'), (2, b'Female')]),
        ),
    ]
