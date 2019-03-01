#!/bin/bash

path='/ftpdata/log/'
outpath='/ftpdata/ftpback/'
if [ ! -d $outpath ]
then
mkdir $outpath
fi 

predate=`date +%Y%m -d -60days`
#echo $predate

for jifanghao in `ls $path`
do
path2="$path$jifanghao/"

for date in `ls $path2|grep $predate`
do
path3="${path2}$date"
#echo $path3

tar czvf ${outpath}${jifanghao}_${date}.tar.gz  ${path3}
sleep 1
rm -rf ${path3}
done

done 
