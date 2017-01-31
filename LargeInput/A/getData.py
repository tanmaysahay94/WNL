#!/bin/env python
# -*- coding: utf-8 -*-

f = open('generatedData.txt', 'a+')

data = open('datafiles/single_sense_a_without_idioms_phras.txt').readlines()

for line in data:
    if line.find('_a_') != -1:
        line = line.split(' _a_ ')
        left = line[0].split()[0]
        right = line[1]
        toPrint = "{} {}\n".format(left, right).strip()
        f.write(toPrint)
        f.write('\n')
    elif len(line) == 1:
        f.write("-\n")
    else:
        f.write(line.strip() + '\n')