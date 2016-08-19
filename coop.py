#!/usr/bin/python
# -*- coding: UTF-8 -*- 

from collections import defaultdict

a = []
dict1 = defaultdict(list)
with open ('test.csv', 'r') as f:
	for line in f:
		line  = line.strip().split('\t')
		a.append(line)

for i, j in a:
	dict1[i].append(j)

b = []
for k in dict1:
	v = '\t'.join([k, str(dict1[k]).decode('gbk').encode('utf-8'), '\n'])
	b.append(v)
	print b

with open('test_res.csv', 'w') as res:
	res.writelines(b)
	res.close()
	f.close()



