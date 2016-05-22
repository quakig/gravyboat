# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 07:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import gravyboat.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20160304_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='code',
            field=models.SlugField(max_length=128, validators=[django.core.validators.RegexValidator(message="Code can only contain the letters a-z, A-Z, digits, and underscores, and can't start with a digit.", regex='^[a-zA-Z_][0-9a-zA-Z_]*$'), gravyboat.core.validators.non_python_keyword], verbose_name='Code'),
        ),
    ]