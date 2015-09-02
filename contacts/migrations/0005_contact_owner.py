# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(to='contacts.UserProfile', null=True),
        ),
    ]
