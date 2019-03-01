#!/bin/bash
LIST="$1"
path="/ftpdata/log"
if [ -d "$path" ]
then
echo " "
else
mkdir /ftpdata/log
fi

error_path="/ftpdata/log/error"
if [ -d "$error_path" ]
then
echo "1"
else
mkdir /ftpdata/log/error
fi

	systemtime2=`date +%Y%m%d`
	ip=`echo $LIST|cut -d ' ' -f 4`
        echo $ip
	if [ `echo $ip|grep ^idcisp-ftp` ]
        then
        echo "1"
        else
        #"zhujimingcuowu"
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        fi

        n1=`echo $LIST | cut -d ' ' -f 7|  awk '{split($0,a,"/" ); print a[length(a)]}' |tr "\"" " "` #wenjianmingcheng
	n2=`echo $LIST | cut -d ' ' -f 12|tr "\"" " "` #wenjiandaxiao
	#p1=`echo $LIST | cut -d ' ' -f 7|cut -d '/' -f 2`
        #p2=`echo $LIST | cut -d ' ' -f 7|cut -d '/' -f 3`
	filetime=`echo $n1|cut -b 1-14`
	systemtime=`date +%Y%m%d%H%M%S`
	#systemtime2=`date +%Y%m%d`

	cn4=`echo $n1|awk '{split($0,a,".");print a[1]}'`
        cn5=`echo $cn4 |awk '{split($0,a,"_");print a[1]}'`
        clen=`echo ${#cn5}`
        #echo $len
        jifanghao=${cn5:clen-5:clen-1}
	#jifanghao=`echo $n1|cut -b 20-24`
        

	if [ `echo $n1|grep ^20 |grep tmp$` ]
        then
        echo "1"
        else
        #buheguifan
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        fi

	if [[ $n2 == *[!0-9]* ]]
        then
        #bushishuzi
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        else
        echo "0"
        fi

	if [[ $filetime == *[!0-9]* ]]
        then
        #bushishuzi
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        else

	if [ `echo $filetime|grep ^20` ]
        then
        echo "1"
        else
        #"bushi20kaitou"
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        fi

        echo "0"
        fi

	if [[ $jifanghao == *[!0-9]* ]]
        then
        #bushishuzi
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        else
        echo "0"
        fi

	day=`echo $n1|cut -b 1-8`
	echo $ip $n1$n2 $systemtime $filetime $jifanghao>>$path/${day}_close.txt
	mv $path/${day}_close.txt $path/${day}_close.txt2
        sort -u $path/${day}_close.txt2 > $path/${day}_close.txt
	rm -rf $path/${day}_close.txt2
        
        logger  -p local5.info "idcisp-close $ip $n1$n2 $systemtime $filetime $jifanghao"


