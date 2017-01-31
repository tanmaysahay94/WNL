#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from nltk.corpus import wordnet as wn

digit = map(lambda x: chr(x + ord("0")), [i for i in range(10)])
digit.append('(')

def cleanData(fileName):
	data = map(lambda x: x.strip(), open(fileName).readlines())
	data = filter(lambda x: len(x), data)
	data = filter(lambda x: x[0] in digit, data)
	data = map(lambda x: ' '.join(x.split()[1:]), data)
	def onlyChar(word):
		return filter(lambda x: x.isalpha(), word)
	data = map(lambda x: x.split()[0].strip() + ' ' + onlyChar(x.split()[-1].strip()), data)
	return '{}\n'.format('\n'.join(data))

def getValidFiles():
	pathToMultiSense = 'Asweta_LEXICONS/Bahari_dict/Multiple_sense_synset/collocation/collocation_**I**/'
	filesToIgnore = ['collocation_a.txt']

	filesMultiSense = filter(lambda x: x not in filesToIgnore, os.listdir(pathToMultiSense))
	filesMultiSense = map(lambda x: pathToMultiSense + x, filesMultiSense)
	filesMultiSense.append('Asweta_LEXICONS/Bahari_dict/Multiple_sense_synset/collocation/collocation_others/collocation_a.txt')
	filesSingleSense = [
		'single_sense_a_ & _adv_without_idioms_phras.txt',
		'single_sense_a_ & _fmc_without_idioms_phras.txt',
		'single_sense_a_ and _fu_without_idioms_phras.txt',
		'single_sense_a_&_mu_without_idioms_phras.txt',
		'single_sense_a_and_fc_without_idioms_phras.txt',
		'single_sense_a_and_mc_without_idioms_phras.txt',
		'single_sense_adv_without_idioms_phras.txt',
		'single_sense_fc_without_idioms_phras.txt',
		'single_sense_fu_without_idioms_phras.txt',
		'single_sense_fuslashc_without_idioms_phras.txt',
		'single_sense_mc_without_idioms_phras.txt',
		'single_sense_mu_slash_c_without_idioms_phras.txt',
		'single_sense_mu_without_idioms_phras.txt'
	]
	pathToSingleSense = 'Asweta_LEXICONS/Bahari_dict/single_sense_synset/Collocation_dict/'
	filesSingleSense = map(lambda x: pathToSingleSense + x, filesSingleSense)
	return filesMultiSense + filesSingleSense

def generateDicts(data):
	hindi_dict = dict()
	english_dict = dict()
	for d in data:
		pair = d.split()
		if len(pair) == 2:
			hindi_dict[pair[0]] = pair[1]
			if not english_dict.has_key(pair[1]):
				english_dict[pair[1]] = list()
			english_dict[pair[1]].append(pair[0])
	return hindi_dict, english_dict

if __name__ == "__main__":
	validFiles = getValidFiles()
	data = ""
	for file in validFiles:
		data += cleanData(file)
	data = data.split('\n')
	h2e, e2h = generateDicts(data)
	for key, val in e2h.iteritems():
		print key,
		for v in val:
			print v,
		print
	for key, val in e2h.iteritems():
		wn.synsets(key)