# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_groupmeta'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='exists_in_group',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
