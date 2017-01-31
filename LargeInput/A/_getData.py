#!/bin/env python
# -*- coding: utf-8 -*-

import re

data = open('datafiles/single_sense_mu_without_idioms_phras.txt').readlines()

f = open('foo.txt', 'a+')

for line in data:
	if line[0] == '(':
		line = re.sub(r'\(\d+\)', '', line)
		line = re.sub(r'\(.*\)', '', line)
		line = line.split(' _mu_ ')
		left = line[0].split()[0].strip()
		right = line[1].split(',')[-1].strip()
		f.write('{} {}\n'.format(left, right))
	elif len(line) == 1:
		f.write('-\n')
	else:
		f.write('{}\n'.format(line.strip()))