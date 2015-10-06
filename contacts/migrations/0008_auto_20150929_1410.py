# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(to='contacts.Category', null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
