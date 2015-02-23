# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadsModel',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.TextField()),
                ('description', models.TextField()),
                ('uploader', models.TextField()),
                ('classification', models.TextField()),
                ('modified', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
