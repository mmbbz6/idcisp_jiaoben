#!/usr/bin/python
# _*_ coding:utf-8 _*_
import json
import ast
import re
import os
import time
from threading import Timer
import sched
import datetime
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import pandas as pd
from pandas import Series,DataFrame

def fun():
        #print('Hello  (%s)\n' % (threading.current_thread().name))
	date = datetime.datetime.now().strftime('%Y%m%d')
	#date = '20180704'
	path = '/ftpdata/log/'
	path_sf = '/ftpdata/shengfen/'
	if not os.path.exists(path_sf):
		os.makedirs(path_sf)
 
	roomlist = os.listdir(path)
	#print date
	for i in roomlist:
		path2 = path + i + '/'
		path_sf2 = path_sf + i + '/'
		if not os.path.exists(path_sf2):
			os.makedirs(path_sf2)
		
		if i.isdigit() and os.path.isdir(path2):
			datelist = os.listdir(path2)
		else:
			continue

		for j in datelist:
			if j == date:
				path3 = path2 + j + '/'
				path_sf3 = path_sf2 + j + '/'
				if not os.path.exists(path_sf3):
					os.makedirs(path_sf3)

				filelist = os.listdir(path3)
				#print filelist
				for k in filelist:
					if k.endswith('rename.txt'):
						filelist_path = path3 + k
						filelist_path_sf = path_sf3 + k
						#print filelist_path_sf 
						data = pd.read_csv(filelist_path,header=None)
						data = data.drop_duplicates()
						#print data
					
						data.to_csv(filelist_path_sf, index=False, header=False)
      #  for k, v in d.items():
                #os.environ['k'] = k
                #os.system('mv $k /ftpdata/sftptemp.txt')
                #os.system('sort -u /ftpdata/sftptemp.txt>$k')
                #os.system('rm -rf /ftpdata/sftptemp.txt')

if __name__ == '__main__':
	fun()
