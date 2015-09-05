# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_contact_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
