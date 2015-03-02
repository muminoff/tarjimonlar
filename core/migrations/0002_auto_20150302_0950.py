# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
    ]
