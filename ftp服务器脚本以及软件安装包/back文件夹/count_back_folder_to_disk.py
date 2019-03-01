# -*- coding: utf-8 -*-
# !/usr/bin/env python
import datetime
import sys
import time
import os
def write2file(d):
        for k, v in d.items():
                with open(k, 'a+') as f:
                        #print k, v
                        for i in range(0,len(v)):
                                #print len(v)
                                f.write('%s,%s,%s,%s,%s,%s\n' % (v[i][0], v[i][1], v[i][2], v[i][3], v[i][4], v[i][5]) )
def fun(date):
        rows=0

        read_path="/ftpdata/log2/"+date+".log"
        d={}

        path="/ftpdata/log4/"
        if not os.path.exists(path):
                os.makedirs(path)

        done = 0
        with open(read_path, 'r') as f:
                while not done:
                        line = f.readline()

                        if line != '':
                                #print line
                                #[hostname, filename, filesize, jifanghao, systemtime, filetime, datefoldername, hour] 
                                ll= line.strip().split(',')  
                                hostname, filename, filesize, jifanghao, systemtime, filetime, datefoldername, hour=ll[0],ll[1],ll[2],ll[3],ll[4],ll[5],ll[6],ll[7]
                  

                                path2=path + jifanghao
                                if not os.path.exists(path2):
                                        os.makedirs(path2)

                                path3=path2 + "/" +  datefoldername
                                if not os.path.exists(path3):
                                        os.makedirs(path3)


                                to_filename_path=path3 + "/" +  hour + ".txt"
                                #filecontents = [hostname, filename, filesize, jifanghao, systemtime, filetime]
                                #print "7777",to_filename_path
                                #if not d.has_key('to_filename_path'):
                                if not to_filename_path in d:
                                        v0=((hostname, filename, filesize, jifanghao, systemtime, filetime),)
                                        #t0=()
                                        d[to_filename_path] = v0
                                        rows += 1
                                        #print "8888",d[to_filename_path],len(d[to_filename_path])
                                else:
                                        v1=d[to_filename_path]
                                        #print v1,'@'
                                        v2 = ((hostname, filename, filesize, jifanghao, systemtime, filetime),)
                                        #print v2,'@@'
                                        d[to_filename_path]= v1 + v2
                                        rows +=1 
                                        #print "999", d[to_filename_path],len(d[to_filename_path])

                       

                                if rows == 3000:
                                        write2file(d)
                                        time.sleep(1)
                                        rows=0
                                        d={}
                        else:
                                done=1
                write2file(d)






if __name__ == '__main__':
        #print sys.argv[1]   
        fun(sys.argv[1])   