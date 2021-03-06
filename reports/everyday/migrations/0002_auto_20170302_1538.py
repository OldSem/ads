# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('everyday', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BUH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
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
            name='DPRS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
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
            name='ES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
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
            name='OKS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
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
            name='OTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
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
            name='OV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
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
        migrations.AddField(
            model_name='dte',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
