# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('everyday', '0005_auto_20170302_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dte',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='everyday.personel'),
        ),
    ]
