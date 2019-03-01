#coding=utf-8
import MySQLdb
import os
import sys
import re

date = sys.argv[1]
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
#cur.execute("create table if not exists idc_rename(hostname varchar(20),filename_old varchar(40), filename_new varchar(40), systemtime varchar(14), filetime varchar(14),roomnumber varchar(10))")
#cur.execute("create table rename(filename varchar(50),filesize varchar(20), roomnumber varchar(10))")

cur.execute("SET @sqlstr = CONCAT('create table if not exists rename_',DATE_FORMAT(CURDATE()-1,'%Y%m%d'),' (hostname varchar(20),filename_old varchar(45), filename_new varchar(45), systemtime varchar(14), filetime varchar(14),roomnumber varchar(10) )')")
cur.execute("SET @tablename=CONCAT('rename_',DATE_FORMAT(CURDATE()-1,'%Y%m%d'))")

cur.execute('select @tablename')
rows = cur.fetchall()
#print "ppp",rows[0][0]
       
cur.execute("PREPARE stmt1 FROM @sqlstr")
try:
        cur.execute("EXECUTE stmt1")
except:
        pass
finally:
        print 'i am continue'

path='/ftpdata/log/'
ftpdata_folder=os.listdir(path)
for i in ftpdata_folder:
        path2=path + i + '/'
        filelist = os.listdir(path2)
        startswith = re.compile(r''+str(date)+'.*')
        endwith = re.compile(r'.*idcisp-rename')

        #print '######',filelist
        for j in filelist:
                #print '######',filelist
                if startswith.match(j) and endwith.match(j):
                        print '@@@@@@@', j
                        filename_path = path2 + j
                        cur.execute("LOAD DATA LOCAL INFILE \"%s\" INTO TABLE %s fields terminated by' '" %(filename_path,rows[0][0]))

#with open("idc_rename.log","r") as f:
#       for line in f:
#               l  = line.strip().split(',')
#               print l
#               cur.execute("insert into idc_rename(hostname,filename_old,filename_new,systemtime,filetime,roomnumber) values(%s,%s,%s,%s,%s,%s)",[l[0],l[1],l[2],l[3],l[4],l[5]])    

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