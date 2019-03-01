#coding=utf-8
import MySQLdb
 
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
#cur.execute("create table if not exists idc_rename(hostname varchar(20),filename_old varchar(40), filename_new varchar(40), systemtime varchar(14), filetime varchar(14),roomnumber varchar(10))")
#cur.execute("create table rename(filename varchar(50),filesize varchar(20), roomnumber varchar(10))")

cur.execute("SET @sqlstr = CONCAT('create table if not exists rename_',DATE_FORMAT(CURDATE(),'%Y%m%d'),' (hostname varchar(20),filename_old varchar(40), filename_new varchar(40), systemtime varchar(14), filetime varchar(14),roomnumber varchar(10) )')")
cur.execute("SET @tablename=CONCAT('rename_',DATE_FORMAT(CURDATE(),'%Y%m%d'))")

cur.execute('select @tablename')
rows = cur.fetchall()
#print "ppp",rows[0][0]
       
cur.execute("PREPARE stmt1 FROM @sqlstr")

cur.execute("EXECUTE stmt1")

cur.execute("LOAD DATA LOCAL INFILE \"/root/idc_rename.log\" INTO TABLE %s fields terminated by' '" %(rows[0][0]))

#with open("idc_rename.log","r") as f:
#       for line in f:
#               l  = line.strip().split(',')
#               print l
#               cur.execute("insert into idc_rename(hostname,filename_old,filename_new,systemtime,filetime,roomnumber) values(%s,%s,%s,%s,%s,%s)",[l[0],l[1],l[2],l[3],l[4],l[5]])    

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