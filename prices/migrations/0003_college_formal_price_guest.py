# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_auto_20151104_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='formal_price_guest',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
        ),
    ]
