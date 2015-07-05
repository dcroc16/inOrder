# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('in_order', '0002_ordertitle_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlistitem',
            name='completed',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
