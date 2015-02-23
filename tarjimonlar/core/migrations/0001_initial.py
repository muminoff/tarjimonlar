# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('message', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('likes', models.IntegerField()),
            ],
            options={
                'ordering': ['-created_time'],
                'db_table': 'comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'members',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('message', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
                ('likes', models.IntegerField()),
                ('creator', models.ForeignKey(to='core.Member')),
            ],
            options={
                'ordering': ['-created_time', '-updated_time'],
                'db_table': 'posts',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(to='core.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='core.Post'),
            preserve_default=True,
        ),
    ]
