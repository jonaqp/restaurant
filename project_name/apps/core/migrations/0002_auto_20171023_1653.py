# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='groupId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='core_role_groupId', to='core.Group', verbose_name='group'),
        ),
        migrations.AlterField(
            model_name='types',
            name='type',
            field=models.CharField(choices=[(0, (('01', 'ACTIVE'), ('02', 'INACTIVE'))), (1, (('01', 'DNI'), ('02', 'RUC'), ('03', 'PASSPORT'))), (2, (('01', 'NATURAL'), ('02', 'JURIDICAL'))), (3, (('01', 'MALE'), ('02', 'FEMALE')))], max_length=10, verbose_name='type'),
        ),
    ]
