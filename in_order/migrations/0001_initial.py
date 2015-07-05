# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderListItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('position', models.IntegerField()),
                ('item', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='OrderTitle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='orderlistitem',
            name='oID',
            field=models.ForeignKey(to='in_order.OrderTitle'),
        ),
    ]
