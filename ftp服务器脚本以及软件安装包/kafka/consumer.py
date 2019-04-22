#!/usr/bin/python
# _*_ coding:utf-8 _*_

from pykafka import KafkaClient
import json
import ast
import re
import os
import time
from threading import Timer
import sched
import datetime
import threading
import threadpool
#import pdb
#import pandas as pd
#from pandas import Series,DataFrame

lock = threading.Lock()
lock2 = threading.Lock()
def fun(d):
	#print('Hello  (%s) **** %s \n' % (threading.current_thread().name, d))
	
	if lock.acquire():
		try:
			for k, v in d.items():
				#print 'kkkkkkkk',k
        			with open(k, 'a+') as f:
                			for i in range(0,len(v)):
                        			f.write('%s %s %s %s %s %s\n' % (v[i][0],v[i][1],v[i][2], v[i][3], v[i][4], v[i][5]) )
     		
		#data = pd.read_csv(k,header=None)
		#data = data.drop_duplicates()
		#data.to_csv(k,index=False,header=False)
 
		#os.environ['k'] = k
		#os.system('mv $k /ftpdata/sftptemp.txt')
		#os.system('sort -u /ftpdata/sftptemp.txt>$k')
		#os.system('rm -rf /ftpdata/sftptemp.txt')
           
		except:
			pass
		finally:
			d.clear()
			balanced_consumer.commit_offsets()
			lock.release()


def error_log_fun(path, msg):
	if lock2.acquire():
        	try:
			with open(path,'a+') as f:
                		f.write('%s\n' %(msg))
        	except:
        		pass
        	finally:
			lock2.release()


def fun2(l1):
	global lock
	rows = 0
	numflag=1
        d = {}
	s1=1
	year = datetime.datetime.now().strftime('%Y') 
	
	path = '/ftpdata/log/'
        if not os.path.exists(path):
        	os.makedirs(path)


	file_error = '/ftpdata/logerror/'
        if not os.path.exists(file_error):
        	os.makedirs(file_error)
	
	for message in balanced_consumer:
    		numflag=1
		if s1 == 1:
			starttime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
			s1 = 0
			
		if message is not None:
        		msg=message.value
			#print('Hello kx (%s) @@@@@@@@@@ %s \n' % (threading.current_thread().name, msg))
			
			msg2=ast.literal_eval(msg)
			msg3 = msg2.get('message')
			msg4 = re.split(r'[\s]+', msg3)
		        
			dict={'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
                        #print '!!!!!!',msg4[0]
			month = dict[msg4[0]] 
			
			if int(msg4[1]) >= 0 and int(msg4[1]) <= 9:
				day = '0' + msg4[1]
			else:
				day = msg4[1]
                        
                        hour, minute, second  = msg4[2].split(':')
			systemtime = year + month + day + hour + minute + second
			hostname = msg4[3] 
			
			

			
			if msg4[5] == 'rename':
				flag = 'idcisp-rename'
				fs = msg4[7].strip('"').split('/')
				filenameold = fs[len(fs)-1]
				filetime_rename = filenameold[0:14]
				filetime_error = systemtime[0:8]
				hour = filenameold[8:10] 
				if not (filetime_rename.isdigit() and filetime_rename.startswith('20')): 
                                        file_error_path = file_error + filetime_error + '_idcisp-rename.txt'
					error_log_fun(file_error_path, msg3)
                                        continue

				
				

				if not (filenameold.startswith('20') and filenameold.endswith('.txt.gz.tmp')):
					file_error_path = file_error + filetime_error + '_idcisp-rename.txt'
                                        error_log_fun(file_error_path, msg3)
					continue

				fs2 = msg4[9].strip('"').split('/')
				filenamenew = fs2[len(fs2)-1]
				if not (filenamenew.startswith('20') and filenamenew.endswith('.txt.gz')):
					file_error_path = file_error + filetime_error + '_idcisp-rename.txt'
                                        error_log_fun(file_error_path, msg3)
					continue

				
				rn = filenamenew.strip('.txt.gz').split('_')
				roomnumber = rn[0][-5:]   
				if not roomnumber.isdigit():
					file_error_path = file_error + filetime_error + '_idcisp-rename.txt'
					error_log_fun(file_error_path, msg3)
                                        continue 
				
				filetime_right = filenameold[0:8]
				#path2 = path + roomnumber_rename + '/'
                                #if not os.path.exists(path2):
                                #        os.makedirs(path2)
				
				#path3 = path2 + filetime_error + '/'
				#if not os.path.exists(path3):
                                #        os.makedirs(path3)

			
				msg4[0],msg4[1],msg4[2],msg4[3],msg4[4],msg4[5] = hostname,filenameold, filenamenew, systemtime, filetime_rename, roomnumber
			else:
				flag = 'idcisp-close'
				fs =  msg4[6].strip('"').split('/')
				filename_close = fs[len(fs)-1]
				hour = filename_close[8:10]  
				filetime_error = systemtime[0:8]
				if not (filename_close.startswith('20') and filename_close.endswith('.txt.gz.tmp')):
                                        file_error_path = file_error + filetime_error + '_idcisp-close.txt'
                                        error_log_fun(file_error_path, msg3)
                                        continue

				filesize = msg4[11] 
				if not filesize.isdigit():
                                        file_error_path = file_error + filetime_error + '_idcisp-close.txt'
                                        error_log_fun(file_error_path, msg3)
                                        continue 

				filetime_close = filename_close[0:14]
				if not (filetime_close.isdigit() and filetime_close.startswith('20')):
                                        file_error_path = file_error + filetime_error + '_idcisp-close.txt'
                                        error_log_fun(file_error_path, msg3)
                                        continue
 
				rn = filename_close.strip('.txt.gz.tmp').split('_')
				roomnumber = rn[0][-5:]
				if not roomnumber.isdigit():
                                        file_error_path = file_error + filetime_error + '_idcisp-close.txt'
                                        error_log_fun(file_error_path, msg3)
                                        continue 
			
				filetime_right = filename_close[0:8]
				#path2 = path + roomnumber_close + '/'  
				#if not os.path.exists(path2):
				#	os.makedirs(path2) 

				#path3 = path2 + filetime_error + '/'
				#if not os.path.exists(path3):
                                #        os.makedirs(path3) 
				msg4[0],msg4[1],msg4[2],msg4[3],msg4[4],msg4[5] = hostname, filename_close, filesize, systemtime, filetime_close, roomnumber

			path2 = path + roomnumber + '/' 
                        if not os.path.exists(path2):
                                try:
					os.makedirs(path2)
				except:
					pass

			path3 = path2 + filetime_right + '/'
                        if not os.path.exists(path3):
                        	try:
					os.makedirs(path3)
				except:
					pass

			filenamepath = path3 +  hour + '_' + flag + '.txt' 
			if not filenamepath in d: 
				v = ((msg4[0],msg4[1],msg4[2],msg4[3],msg4[4],msg4[5]),)
				d[filenamepath] = v
				#print ',,,,,,', filenamepath,d
				rows += 1
			else:
				v0 = d[filenamepath]
				#vv = (msg4[0],msg4[1],msg4[2],msg4[3],msg4[4],msg4[5])
				#if not vv in v0:
				v1 = ((msg4[0],msg4[1],msg4[2],msg4[3],msg4[4],msg4[5]),)
				d[filenamepath] = v0 + v1
				#print '//////////',filenamepath, d
				rows += 1	
			
			if rows == 1000:
				fun(d)
				rows=0
				s1=1
				numflag=0
						
	
		
		endtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
		duration = int(endtime) - int(starttime)
		if duration >= 1800 and numflag==1:
			fun(d)
			s1=1
			rows=0
					
					


if __name__ == '__main__':
        client=KafkaClient(hosts='10.0.8.51:9092,10.0.8.52:9092,10.0.8.53:9092')
        topic=client.topics['kafkaftp']
	

        balanced_consumer = topic.get_balanced_consumer(
        reset_offset_on_start=False,
        consumer_group='testgroup',
        auto_commit_enable=False,
        zookeeper_connect='10.0.8.51:2181,10.0.8.52:2181,10.0.8.53:2181'
        )
	pool = threadpool.ThreadPool(10)
	#l1=[1,2]
	l1=[1,2,3,4,5,6,7,8,9,10]
	tasks = threadpool.makeRequests(fun2, l1)
	#print('tasks', len(tasks))
	[pool.putRequest(task) for task in tasks]
	pool.wait()

