#!/bin/bash

path='/ftpdata/shengfen/' 

predate=`date +%Y%m -d -30days`

for jifanghao in `ls $path`
do
path2="$path$jifanghao/"

for date in `ls $path2|grep $predate`
do
path3="${path2}$date"
rm -rf ${path3}
done

done 
