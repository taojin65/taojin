#!/usr/bin/python
# -*- coding: UTF-8 -*- 

with open('test.csv', 'r')  as f:
	total = 0
	for line in f:
		print line
		total += int(line.strip())
		print '%s' % total 