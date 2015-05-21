# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_exists_in_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='exists_in_group',
        ),
    ]
