# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='co_respuesta',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
