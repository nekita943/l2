# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0034_auto_20161107_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issledovaniya',
            name='lab_comment',
            field=models.TextField(blank=True, default='', help_text='Комментарий, оставленный лабораторией', null=True),
        ),
    ]