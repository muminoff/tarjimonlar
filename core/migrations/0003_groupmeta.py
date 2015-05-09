# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_member_currently_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMeta',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'groupinfo',
            },
            bases=(models.Model,),
        ),
    ]
