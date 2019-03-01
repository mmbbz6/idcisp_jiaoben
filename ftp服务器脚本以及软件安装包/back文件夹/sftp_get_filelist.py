# -*- coding: utf-8 -*-
# !/usr/bin/env python
import paramiko
import re 
def fun():
        t = paramiko.Transport(("10.0.108.16", 22))
        t.connect(username='test2', password='8a9z3c2H')
        sftp = paramiko.SFTPClient.from_transport(t)
        print(sftp.retrlines('MLSD'))
        files = sftp.listdir('/ftpdata')
        saved_files=[]
        endwith=re.compile('.*_fdr_back')
        for i in range(0,len(files)):
                if endwith.match(files[i]):
                        print files[i], 
if __name__ == '__main__':
        print(dir("SFTPClient"))
        fun()