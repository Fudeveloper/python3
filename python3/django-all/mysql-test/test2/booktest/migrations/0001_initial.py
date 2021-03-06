# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField()),
                ('bread', models.IntegerField(default=0)),
                ('bcoment', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'lalala',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
                ('hcontent', models.CharField(max_length=40)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
