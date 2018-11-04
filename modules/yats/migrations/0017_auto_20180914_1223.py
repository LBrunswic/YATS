# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-14 10:23
from __future__ import unicode_literals

from django.db import migrations

def checkHasComments(apps, schema_editor):
    tickets = apps.get_model('yats', 'tickets')
    comments = apps.get_model('yats', 'tickets_comments')
    for ticket in tickets.objects.all():
        if comments.objects.filter(ticket=ticket.pk).count() > 0:
            ticket.hasComments = True
            ticket.save()

class Migration(migrations.Migration):

    dependencies = [
        ('yats', '0016_tickets_hascomments'),
    ]

    operations = [
        migrations.RunPython(checkHasComments),
    ]