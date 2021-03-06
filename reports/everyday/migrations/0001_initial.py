# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DTE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nn', models.CharField(max_length=10)),
                ('work', models.CharField(max_length=200)),
                ('ESN', models.CharField(max_length=10)),
                ('adress', models.CharField(max_length=200)),
                ('rezult', models.CharField(max_length=10)),
                ('executor', models.CharField(max_length=20)),
                ('elapsed_time', models.CharField(max_length=5)),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
