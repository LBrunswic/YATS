# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-22 22:24
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify

def create_slug(apps, schema_editor):
    reports = apps.get_model('yats', 'tickets_reports')
    for rep in reports.objects.all():
        rep.slug = slugify(rep.name)
        rep.save()

class Migration(migrations.Migration):

    dependencies = [
        ('yats', '0006_tickets_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets_reports',
            name='slug',
            field=models.SlugField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.RunPython(create_slug),
    ]
