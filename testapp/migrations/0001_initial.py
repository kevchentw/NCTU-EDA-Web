# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testapp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tid', models.IntegerField()),
                ('char', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('integer', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
