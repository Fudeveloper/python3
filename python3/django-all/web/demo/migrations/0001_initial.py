# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchSwitch',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('open', models.BooleanField(default=False)),
                ('pname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('current', models.FloatField()),
                ('load_current', models.FloatField()),
                ('pname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Environmant',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('wind', models.CharField(max_length=30)),
                ('exhaust', models.CharField(max_length=30)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('light_open', models.BooleanField(default=False)),
                ('pname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LightningProtect',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('pname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('pname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('plan_number', models.IntegerField()),
                ('finish_number', models.IntegerField()),
                ('pname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('open', models.BooleanField(default=False)),
                ('pname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('pname', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('pname', models.CharField(max_length=30)),
            ],
        ),
    ]
