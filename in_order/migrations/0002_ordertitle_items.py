# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('in_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertitle',
            name='items',
            field=models.ManyToManyField(to='in_order.OrderListItem'),
        ),
    ]
