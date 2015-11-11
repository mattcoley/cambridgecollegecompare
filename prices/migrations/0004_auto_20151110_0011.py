# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0003_college_formal_price_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='num_of_graduates',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='num_of_incoming',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='num_of_undergraduates',
            field=models.IntegerField(default=0),
        ),
    ]
