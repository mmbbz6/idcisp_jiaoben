#!/bin/bash

LIST="$1"
path="/ftpdata/log"
if [ -d "$path" ]
then
echo "1"
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

        systemtime=`date +%Y%m%d%H%M%S`
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

        n1=`echo $LIST | cut -d ' ' -f 7|awk '{split($0,a,"/" ); print a[length(a)]}' |tr "\"" " "` #wenjianmingcheng
        n2=`echo $LIST | cut -d ' ' -f 12` #wenjiandaxiao
        #p1=`echo $LIST | cut -d ' ' -f 7|cut -d '/' -f 2`
        #p2=`echo $LIST | cut -d ' ' -f 7|cut -d '/' -f 3`
        echo $n1
        if [ `echo $n1|grep ^20 |grep tmp$` ]
        then  
        echo "1"
        else
        #buheguifan
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        fi

        datefoldername=`echo $n1|cut -b 1-8`
        if [[ $datefoldername == *[!0-9]* ]]
        then
        #bushishuzi
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        else

        if [ `echo $datefoldername|grep ^20` ]
        then
        echo "1"
        else
        #"bushi20kaitou"
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        fi

        echo "0"
        fi




        filetime=`echo $n1|cut -b 1-14`
        
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

        jifanghao=`echo $n1|cut -b 20-24`
        echo $jifanghao
        if [[ $jifanghao == *[!0-9]* ]]
        then
        #bushishuzi
        echo $LIST>>/ftpdata/log/error/close_error_${systemtime2}.log
        exit
        else
        echo "0"
        fi



          path2="$path/$jifanghao"
        if [ -d "$path2" ]
        then
        echo "1"
        else
        echo "0"
        mkdir /ftpdata/log/${jifanghao}
        fi


        path3="$path/$jifanghao/$datefoldername"
        if [ -d "$path3" ]
        then
        echo "111"
        else
        echo "0000"
        mkdir /ftpdata/log/${jifanghao}/${datefoldername}
        fi

        hour=`echo $n1|cut -b 9-10`
        

       

        echo $ip $n1$n2 $systemtime $filetime $jifanghao>>$path3/${hour}_close.txt
