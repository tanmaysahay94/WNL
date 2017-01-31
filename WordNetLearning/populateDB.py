#!/bin/env python
# -*- coding: utf-8 -*-

import django
django.setup()

from trainingInterface.models import Record

data = open('../generatedData.txt').readlines()
data = [line.strip() for line in data]

h_word = ''
e_meaning = ''
e_examples = ''

for line in data:
	if len(line) == 0:
		continue
	if len(line.split()) == 2:
		h_word, e_meaning = line.split()
	if line[0] == '-':
		try:
			r = Record(hindi_word=h_word, english_meaning=e_meaning, examples=e_examples)
			r.save()
			h_word = ''
			e_meaning = ''
			e_examples = ''
		except:
			h_word = ''
			e_meaning = ''
			e_examples = ''
	else:
		e_examples += '{}\n'.format(line)