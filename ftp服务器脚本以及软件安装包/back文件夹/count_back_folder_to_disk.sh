#!/bin/bash

argc=$#
if [ ! $argc -eq 1 ]
then
echo "input date example bash count_back_folder_to_disk.sh 20180607"
fi

path="/ftpdata/log2"

        if [ ! -d "$path" ]
        then
        mkdir /ftpdata/log2
        fi

date=$1
IFS_old=$IFS
IFS=$'\n'
cat /ftpdata/log2/${date}.log|while read line
do
#echo $line
eval $(echo $line |awk -F ',' '{printf("hostname=%s;filename=%s;filesize=%s;jifanghao=%s;systemtime=%s;filetime=%s;datefoldername=%s;hour=%s;",$1,$2,$3,$4,$5,$6,$7,$8) }')
#echo $filename,$datefoldername

        path2="$path/$jifanghao"
        if [ ! -d "$path2" ]
        then
        mkdir /ftpdata/log2/${jifanghao}
        fi 

         path3="$path/$jifanghao/$datefoldername"
        if [ ! -d "$path3" ]
        then
        mkdir /ftpdata/log2/${jifanghao}/${datefoldername}
        fi

       #echo $path3,$hour
        echo $hostname $filename $filesize $jifanghao $systemtime $filetime>> $path3/${hour}.txt

done
IFS=$IFS_old