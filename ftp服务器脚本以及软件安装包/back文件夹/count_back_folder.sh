#!/bin/sh
#scan_directory_file_number /ftpdata/*_fdr_bak/ /ftpdata/*_error_bak/ 
        argc=$#
        #echo "ppp", $#
        if [ ! $argc -eq 1 ]
        then
        echo "input date example: bash count_back_folder 20180607"
        fi

        path="/ftpdata/log2"

        if [ ! -d "$path" ]
        then
        mkdir /ftpdata/log2
        fi

        error_path="/ftpdata/log2/error"
        if [ ! -d "$error_path" ]
        then
        mkdir /ftpdata/log2/error
        fi

    export TIME_STYLE='+%Y%m%d%H%M%S'



    date=$1


        for j1 in `ls /ftpdata/| grep _fdr_bak`
        do
                echo $j1
                IFS_old=$IFS
                IFS=$'\n'
                for j2 in `ls -lh /ftpdata/$j1/|sed '1d'|grep $date`
                do
                echo "j2",$j2
                filesize=`echo $j2|sed "s/\s\+/ /g"|cut -d ' ' -f 5` # >> /home/hjx/${date}_fdr_back.txt;
                systemtime=`echo $j2|sed "s/\s\+/ /g"|cut -d ' ' -f 6`
                filename=`echo $j2|sed "s/\s\+/ /g"|cut -d ' ' -f 7`
                echo "filename",$filename
                filetime=`echo $filename|cut -b 1-14`
                datefoldername=`echo $filename|cut -b 1-8`
                hour=`echo $filename|cut -b 9-10`  
                jifanghao=`echo $filename|cut -b 20-24`

                hostname=`hostname`
                #echo $hostname
                if [ ! `echo $hostname|grep ^idcisp-ftp` ]
                then
                #"zhujimingcuowu"
                echo "/ftpdata/$j1/$filename",$hostname>>/ftpdata/log2/error/error_${date}.log
                continue
                fi

                if [ ! `echo $filename|grep ^20 |grep gz$` ]
        then
        #buheguifan
        echo "/ftpdata/$j1/$filename",$hostname>>/ftpdata/log2/error/error_${date}.log
                continue
        fi

                if [[ $datefoldername == *[!0-9]* ]]
        then
        #bushishuzi
        echo "/ftpdata/$j1/$filename",$hostname>>/ftpdata/log2/error/error_${date}.log
        continue
                else

        if [ ! `echo $datefoldername|grep ^20` ]
        then
        #"bushi20kaitou"
        echo "/ftpdata/$j1/$filename",$hostname>>/ftpdata/log2/error/error_${date}.log
                continue
        fi

                echo "0"
        fi


                if [[ $jifanghao == *[!0-9]* ]]
        then
        #bushishuzi
        echo "/ftpdata/$j1/$filename",$hostname>>/ftpdata/log2/error/error_${date}.log
                continue
        fi

                if [[ $filetime == *[!0-9]* ]]
        then
        #bushishuzi
        echo "/ftpdata/$j1/$filename",$hostname>>/ftpdata/log2/error/error_${date}.log
                continue
        else

        if [ ! `echo $filetime|grep ^20` ]
        then
        #"bushi20kaitou"
        echo "/ftpdata/$j1/$filename",$hostname>>/ftpdata/log2/error/error_${date}.log
                continue
        fi

        echo "0"
        fi
                echo $hostname,$filename,$filesize,$jifanghao,$systemtime,$filetime,$datefoldername,$hour >> /ftpdata/log2/${date}.log
        done
        IFS=$IFS_old
        done