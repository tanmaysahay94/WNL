#!/bin/env python
# -*- coding: utf-8 -*-

import os
os.system('export DJANGO_SETTINGS_MODULE=WordNetLearning.settings')

import django
django.setup()

from trainingInterface.models import Record

word = raw_input()

r = Record.objects.all().filter(english_meaning=word)

for s in r:
    print s.hindi_word, s.english_meaning, s.sense
