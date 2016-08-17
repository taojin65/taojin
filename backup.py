#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os, time, zipfile

## 路径
goal_path = '/Users/taojin/Desktop/python'
back_up_path = '/Users/taojin/Desktop/back_up' + os.sep + time.strftime("%Y%m%d", time.localtime())
back_up_doc_name = back_up_path + os.sep + time.strftime("%Y%m%d", time.localtime()) + '.' + 'zip'

if os.path.isdir(goal_path) == False:
	print '待备份文件夹不存在,'
	exit()

if os.path.isdir(back_up_path) == False:
	os.makedirs(back_up_path)

if os.path.isfile(back_up_doc_name):
	print '备份文件已存在'
	exit()
else:
	back_up_doc = zipfile.ZipFile(back_up_doc_name ,'w',zipfile.ZIP_DEFLATED)
	for file in os.listdir(goal_path):
		back_up_doc.write(os.path.join(goal_path, file), file)
	back_up_doc.close()
	print 'done'
	print '成功备份>>%s' % back_up_doc_name
