#!/bin/bash
path="/ftpdata/log/"
c=0
for i in `ls $path`
do
for j in `ls $path$i`
do

if [ $j == $1 ]
then
echo $j
for k in `ls $path$i/$j`
do
n=`wc -l  $path$i/$j/$k|cut -d ' ' -f 1`
echo $n
let c=c+n
done

fi
done
done
echo $c  