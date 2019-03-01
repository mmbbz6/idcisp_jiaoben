#!/bin/bash
path="/ftpdata/log"
#echo $1>>/var/log/cccc.txt
LIST="$1"
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
		
        n3=`echo $LIST | cut -d ' ' -f 8| awk '{split($0,a,"/" ); print a[length(a)]}' |tr "\"" " " ` #wenjianmingcheng rename old
        n9=`echo $LIST | cut -d ' ' -f 10| awk '{split($0,a,"/" ); print a[length(a)]}'  |tr "\"" " "` #wenjianmingcheng rename new
        #p1=`echo $LIST | cut -d ' ' -f 10|cut -d '/' -f 2` 
        #p2=`echo $LIST | cut -d ' ' -f 10|cut -d '/' -f 3`
        echo 'pp',$n3>>/var/log/cccc.txt
        echo 'qq',$n9>>/var/log/cccc.txt

        datefoldername=`echo $n3|cut -b 1-8`
        filetime=`echo $n3|cut -b 1-14`
        systemtime=`date +%Y%m%d%H%M%S`
		systemtime2=`date +%Y%m%d`
        #echo $systemtime
        #echo $filetime

        jifanghao=`echo $n3|cut -b 20-24`
        echo $jifanghao

        if [ `echo $n3|grep ^20 |grep tmp$` ]
        then
        echo "1"
        else
        #buheguifan
        echo $LIST>>/ftpdata/log/error/rename_error_${systemtime2}.log
        exit
        fi

        if [ `echo $n9|grep ^20 |grep gz$` ]
        then
        echo "1"
        else
        #buheguifan
        echo $LIST>>/ftpdata/log/error/rename_error_${systemtime2}.log
        exit
        fi

        if [[ $jifanghao == *[!0-9]* ]]
        then
        #bushishuzi
        echo $LIST>>/ftpdata/log/error/rename_error_${systemtime2}.log
        exit
        else
        echo "0"
        fi

        if [[ $datefoldername == *[!0-9]* ]]
        then
        #bushishuzi
        echo $LIST>>/ftpdata/log/error/rename_error_${systemtime2}.log
        exit
        else

        if [ `echo $datefoldername|grep ^20` ]
        then
        echo "1"
        else
        #"bushi20kaitou"
        echo $LIST>>/ftpdata/log/error/rename_error_${systemtime2}.log
        exit
        fi

        echo "0"
        fi


        if [[ $filetime == *[!0-9]* ]]
        then
        #bushishuzi
        echo $LIST>>/ftpdata/log/error/rename_error_${systemtime2}.log
        exit
        else

        if [ `echo $filetime|grep ^20` ]
        then
        echo "1"
        else
        #"bushi20kaitou"
        echo $LIST>>/ftpdata/log/error/rename_error_${systemtime2}.log
        exit
        fi

        echo "0"
        fi

        path2="$path/$jifanghao"
        if [ -d "$path2" ]
        then
        echo "111"
        else
        echo "0000"
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

        
        hour=`echo $n3|cut -b 9-10`
        echo "ddsee#$hour"


        echo $ip $n3$n9$systemtime $filetime $jifanghao>> $path3/${hour}_rename.txt