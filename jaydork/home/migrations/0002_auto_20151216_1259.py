# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='confirm_password',
            field=models.CharField(max_length=10, default=None),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=20, default=None),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, default=None),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=10, default=None),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=15, default=None),
        ),
    ]
