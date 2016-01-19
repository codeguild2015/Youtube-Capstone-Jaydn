# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151216_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='confirm_password',
        ),
    ]
