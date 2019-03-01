# -*- coding: UTF8 -*-
# !/usr/bin/env python

import time
import datetime
import os 
import re
import sys
  
def TimeStampToTime(timestamp):
        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y%m%d%H%M%S',timeStruct)

def get_FileSize(filePath):
        filePath = unicode(filePath,'utf8')
        fsize = os.path.getsize(filePath)
        fsize = fsize/float(1024*1024)
        return round(fsize,2)

def get_FileCreateTime(filePath):
        filePath = unicode(filePath,'utf8')
        t = os.path.getctime(filePath)
        return TimeStampToTime(t)

def fun(date):
        host = os.popen('echo $HOSTNAME')
        try:
                hostname = host.read().strip()
                #print hostname
        finally:
                host.close()

        path="/ftpdata"
        fdr_bak=[]
        if os.path.exists(path):
                dirs = os.listdir(path)
                endwith = re.compile(r'.*_fdr_bak')
                for i in dirs:
                        if endwith.match(i):
                                fdr_bak.append(i)
                                #print i


                for i in fdr_bak:
                        path2 = path + "/" + i
                        filelist=os.listdir(path2)
                        startwith = re.compile(r''+str(date)+'.*')

                        for filename in filelist:
                                if startwith.match(filename):
                                        filename_path = path2 + "/" + filename
                                        filename_time = filename[0:14]
                                        datefoldername = filename[0:8]
                                        jifanghao = filename[19:24]
                                        hour = filename[8:10]
                                        file_size = os.path.getsize(filename_path)
                                        file_create_system_time = get_FileCreateTime(filename_path)
                                        #print hostname, filename, file_size, jifanghao, file_create_system_time, filename_time, datefoldername, hour
                                        outputpath= "/ftpdata/log2/" + date + ".log"
                                        #print outputpath 
                                        with open(outputpath, "a+") as f:
                                                #f.write('%s' %(outputpath))
                                                f.write('%s,%s,%s,%s,%s,%s,%s,%s\n' % (hostname, filename, file_size, jifanghao, file_create_system_time, filename_time, datefoldername, hour)) 
if __name__ == '__main__':
        fun(sys.argv[1])