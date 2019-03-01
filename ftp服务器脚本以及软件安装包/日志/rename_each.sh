#!/bin/bash
path="/ftpdata/log"
LIST="$1"
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

        ip=`echo $LIST|cut -d ' ' -f 4`
        echo $ip

        n6=`echo $LIST | cut -d ' ' -f 6`
        if [ $n6 == 'idcisp-rename' ]
        then
        echo " "
        exit
        fi

        n3=`echo $LIST | cut -d ' ' -f 8| awk '{split($0,a,"/" ); print a[length(a)]}'  |tr "\"" " " ` #wenjianmingcheng rename old
        n9=`echo $LIST | cut -d ' ' -f 10| awk '{split($0,a,"/" ); print a[length(a)]}'   |tr "\"" " "` #wenjianmingcheng rename new
        #p1=`echo $LIST | cut -d ' ' -f 10|cut -d '/' -f 2` 
        #p2=`echo $LIST | cut -d ' ' -f 10|cut -d '/' -f 3`
        echo $n3

        #n3='201808010900113203200131003.txt.gz'
        cn4=`echo $n3|awk '{split($0,a,".");print a[1]}'`
        cn5=`echo $cn4 |awk '{split($0,a,"_");print a[1]}'`
        clen=`echo ${#cn5}`
        #echo $len
        jifanghao=${cn5:clen-5:clen-1}

        #jifanghao=`echo $n3|cut -b 20-24`
        echo $jifanghao


        filetime=`echo $n3|cut -b 1-14`
        systemtime=`date +%Y%m%d%H%M%S`
        systemtime2=`date +%Y%m%d`
        day=`echo $n3|cut -b 1-8`

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
 
        echo $ip $n3$n9$systemtime $filetime $jifanghao>> $path/${day}_rename.txt
        mv $path/${day}_rename.txt $path/${day}_rename.txt2
        sort -u $path/${day}_rename.txt2 > $path/${day}_rename.txt
        rm -rf $path/${day}_rename.txt2
        logger  -p local5.info "idcisp-rename $ip $n3$n9$systemtime $filetime $jifanghao"