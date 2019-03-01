#!/bin/bash
ip=10.0.8.
ip2=10.0.9.
total=0
for i in {2..42}
do
c=0
r1=`ssh root@${ip}$i "wc -l /ftpdata/log/$1_rename.txt"`
echo ${ip}$i
c1=`echo $r1|cut -d " " -f 1`
echo $c1

r2=`ssh root@${ip}$i "wc -l /ftpdata/log/$1_close.txt"`
c2=`echo $r2|cut -d " " -f 1`
echo $c2

let c=c1+c2
echo $c
let total=total+c
done


for i in {45..64}
do
c=0
r1=`ssh root@${ip}$i "wc -l /ftpdata/log/$1_rename.txt"`
echo ${ip}$i
c1=`echo $r1|cut -d " " -f 1`
echo $c1

r2=`ssh root@${ip}$i "wc -l /ftpdata/log/$1_close.txt"`
c2=`echo $r2|cut -d " " -f 1`
echo $c2

let c=c1+c2
echo $c
let total=total+c
done


for i in {1..35}
do
c=0
echo ${ip2}$i
r1=`ssh root@${ip2}$i "wc -l /ftpdata/log/$1_rename.txt"`
c1=`echo $r1|cut -d " " -f 1`
echo $c1

r2=`ssh root@${ip2}$i "wc -l /ftpdata/log/$1_close.txt"`
c2=`echo $r2|cut -d " " -f 1`
echo $c2

let c=c1+c2
echo $c
let total=total+c
done
 

for i in {37..41}
do
c=0
echo ${ip2}$i
r1=`ssh root@${ip2}$i "wc -l /ftpdata/log/$1_rename.txt"`
c1=`echo $r1|cut -d " " -f 1`
echo $c1

r2=`ssh root@${ip2}$i "wc -l /ftpdata/log/$1_close.txt"`
c2=`echo $r2|cut -d " " -f 1`
echo $c2

let c=c1+c2
echo $c
let total=total+c
done


for i in {43..65}
do
c=0
echo ${ip2}$i
r1=`ssh root@${ip2}$i "wc -l /ftpdata/log/$1_rename.txt"`
c1=`echo $r1|cut -d " " -f 1`
echo $c1

r2=`ssh root@${ip2}$i "wc -l /ftpdata/log/$1_close.txt"`
c2=`echo $r2|cut -d " " -f 1`
echo $c2

let c=c1+c2
echo $c
let total=total+c
done

echo $total