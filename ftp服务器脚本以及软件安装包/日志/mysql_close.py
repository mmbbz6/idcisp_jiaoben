#coding=utf-8
import MySQLdb
import re
import os
import sys

date = sys.argv[1]
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='8a9z3c2H!@#',
        db ='test',
        )
cur = conn.cursor()


#�������ݱ�
#cur.execute("create table idc_close(filename varchar(40),filesize varchar(20),filerows varchar(10))")

#concat('create table TABLE_',date_format(curdate(),'%Y%m%d'),' (id int)');
#PREPARE stmt1 FROM @sqlstr ;
#EXECUTE stmt1 ;
cur.execute("SET @sqlstr = CONCAT('create table if not exists close_',DATE_FORMAT(CURDATE()-1,'%Y%m%d'),' (hostname varchar(20),filename varchar(45),filesize varchar(30), systemtime varchar(14),filetime varchar(14),roomnumber varchar(5)  )')")
cur.execute("SET @tablename=CONCAT('close_',DATE_FORMAT(CURDATE()-1,'%Y%m%d'))")

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
        filelist = os.listdir(path2)
        startswith = re.compile(r''+str(date)+'.*')
        endwith = re.compile(r'.*idcisp-close')

        #print '######',filelist
        for j in filelist:
                #print '######',filelist
                if startswith.match(j) and endwith.match(j):
                        print '@@@@@@@', j
                        filename_path = path2 + j
                        cur.execute("LOAD DATA LOCAL INFILE \"%s\" INTO TABLE %s fields terminated by' '" %(filename_path,rows[0][0]))
#with open("idc_close.log","r") as f:
#       for line in f:
#               l  = line.strip().split(',')
#               print l
#
#               cur.execute("insert into idc_close(filename,filesize,systemtime,filetime,roomnumber) values(%s,%s)",[l[0],l[1],l[2],l[3],l[4]])    

#����һ������
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

#cur.execute('select * from student')
#rows = cur.fetchall()
#print(rows) 

#�޸Ĳ�ѯ����������
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#ɾ����ѯ����������
#cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()