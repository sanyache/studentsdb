# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20170514_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0430'),
        ),
    ]