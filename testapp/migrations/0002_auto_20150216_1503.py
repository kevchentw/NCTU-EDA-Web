# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testapp',
            name='id',
        ),
        migrations.AlterField(
            model_name='testapp',
            name='tid',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
