# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('upd_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
    ]