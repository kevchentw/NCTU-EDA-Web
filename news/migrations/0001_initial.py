# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('top', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(editable=False)),
                ('modified_time', models.DateTimeField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('author', models.TextField()),
                ('classification', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
