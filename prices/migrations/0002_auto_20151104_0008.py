# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='college_age',
        ),
        migrations.AddField(
            model_name='college',
            name='food_price',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='college',
            name='formal_price',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='college',
            name='rent_price',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='college',
            name='college_name',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
