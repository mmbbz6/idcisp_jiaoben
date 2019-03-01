#coding=utf-8
import sys
sys.path.append("/usr/lib64/python2.6/site-packages")
import MySQLdb
import re
import os
import datetime

#date = sys.argv[1]
date = datetime.datetime.now().strftime('%Y%m%d')

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='8a9z3c2H!@#',
        db ='test',
        )
cur = conn.cursor()


#创建数据表
#cur.execute("create table idc_close(filename varchar(40),filesize varchar(20),filerows varchar(10))")

#concat('create table TABLE_',date_format(curdate(),'%Y%m%d'),' (id int)');
#PREPARE stmt1 FROM @sqlstr ;
#EXECUTE stmt1 ;
cur.execute("SET @sqlstr = CONCAT('create table if not exists close_',DATE_FORMAT(CURDATE(),'%Y%m%d'),' (hostname varchar(20),filename varchar(45),filesize varchar(30), systemtime varchar(14),filetime varchar(14),roomnumber varchar(5)  )')")
cur.execute("SET @tablename=CONCAT('close_',DATE_FORMAT(CURDATE(),'%Y%m%d'))")

cur.execute('select @tablename')
rows = cur.fetchall()
#print "ppp",rows[0][0]
       
cur.execute("PREPARE stmt1 FROM @sqlstr")

cur.execute("EXECUTE stmt1")
#cur.execute("create table idc_close_',DATE_FORMAT(CURDATE(),'%Y%m%d'),'(filename varchar(40),filesize varchar(30))")
#cur.execute("create table rename(filename varchar(50),filesize varchar(20), roomnumber varchar(10))")

path='/ftpdata/log/'
ftpdata_folder=os.listdir(path)
for i in ftpdata_folder:
        path2=path + i + '/'
        if i.isdigit() and os.path.isdir(path2):
		datelist = os.listdir(path2)
	else:
		continue

        startswith = re.compile(r''+str(date)+'.*')
        endwith = re.compile(r'.*idcisp-close')

        #print '######',filelist
        for j in datelist:
                #print '######',filelist
                if startswith.match(j):
                        #print '@@@@@@@', j
			path3 = path2 + j + '/'
			filelist = os.listdir(path3)
			for k in filelist:
				if endwith.match(k):
                        		filename_path = path3 + k
					cur.execute("LOAD DATA LOCAL INFILE \"%s\" INTO TABLE %s fields terminated by' '" %(filename_path,rows[0][0]))
#with open("idc_close.log","r") as f:
#       for line in f:
#               l  = line.strip().split(',')
#               print l
#
#               cur.execute("insert into idc_close(filename,filesize,systemtime,filetime,roomnumber) values(%s,%s)",[l[0],l[1],l[2],l[3],l[4]])    

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

#cur.execute('select * from student')
#rows = cur.fetchall()
#print(rows) 

#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()
