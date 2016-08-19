#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from collections import defaultdict

a = []
dict1 = defaultdict(list)
with open ('test.csv', 'r') as f:
	for line in f:
		line  = line.strip().split('\t')
		a.append(line)

for i, j in a:
	dict1[i].append(j)

for k ,v in dict1.items():
	print '%s\t%s' % (k, v)

'''
b = []
for k in dict1:
	v = '\t'.join([k, str(dict1[k]), '\n'])
	b.append(v)

with open('test_res.csv', 'w') as res:
	res.writelines(b)
	res.close()
	f.close()
'''


