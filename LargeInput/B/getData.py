#!/bin/env python
# -*- coding: utf-8 -*-

with open('generatedData.txt', 'a+') as f:
	data = open('datafiles/collocation_a.txt').readlines()
	for line in data:
		line = line.strip()
		if len(line) == 0:
			f.write('-\n')
			continue
		toWrite = ""
		if len(line) and line[0].isdigit():
			foo = line.split(';')[0].split(':')[0]
			foo = foo.split(',')[0]
			foo = foo.split()
			toWrite = "{} {}".format(foo[1], foo[4])
		elif len(line):
			toWrite = line
		f.write("{}\n".format(toWrite))