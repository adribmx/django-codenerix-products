# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-10 12:36
from __future__ import unicode_literals

import codenerix.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0041_auto_20171108_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfinaltexten',
            name='description_sample',
            field=codenerix.fields.WysiwygAngularField(blank=True, null=True, verbose_name='Sample description'),
        ),
        migrations.AddField(
            model_name='productfinaltextes',
            name='description_sample',
            field=codenerix.fields.WysiwygAngularField(blank=True, null=True, verbose_name='Sample description'),
        ),
    ]
