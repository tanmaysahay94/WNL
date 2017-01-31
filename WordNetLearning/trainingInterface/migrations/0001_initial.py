# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hindi_word', models.CharField(max_length=64, unique=True)),
                ('english_meaning', models.CharField(max_length=128)),
                ('examples', models.CharField(max_length=1024)),
                ('sense', models.IntegerField(null=True)),
            ],
        ),
    ]