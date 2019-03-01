#!/bin/bash
ip=` ifconfig -a|grep inet|grep  10.0.|grep -v inet6|awk '{print $2}'|tr -d "addr:"|tr "\n" " " `
echo $ip

while getopts 'l:' OPT; do
    case $OPT in
        l)
            LIST="$OPTARG";;
        ?)
            echo "Usage: `basename $0` -l "要搜索的文件列表文件"  -n "需要抽取多少个手机号码" -f "msisdn在第几个字段""
    esac
done

optnum=$(($OPTIND - 1))

shift $(($OPTIND - 1))

if [ $optnum -ne 2 ];then
        echo "Usage: `basename $0` -l "要搜索的文件列表文件"  -n "需要抽取多少个手机号码" -f "msisdn在第几个字段"
                在文件列表的文件中抽取若干个手机号,需要用-f参数指定msisdn在文件第几个字段 "
        exit
fi
echo $LIST

path="/ftpdata/log"
if [ -d "$path" ]
then
echo "111"
else
echo "0000"
mkdir /ftpdata/log
fi

k1=`echo $LIST|grep rename`
k2=`echo $LIST|grep close`


if [ ! -n "$k1" ]
        then

        n1=`echo $LIST | cut -d ' ' -f 7|cut -d '/' -f 4|cut -b 1-31 ` #wenjianmingcheng
	n2=`echo $LIST | cut -d ' ' -f 12` #wenjiandaxiao
	p1=`echo $LIST | cut -d ' ' -f 7|cut -d '/' -f 2`
        p2=`echo $LIST | cut -d ' ' -f 7|cut -d '/' -f 3`
	echo $n1

	jifanghao=`echo $n1|cut -b 20-24`
        echo $jifanghao

	w1=`wc -l /$p1/$p2/$n1|cut -d ' ' -f 1` #wenjianhangshu
        echo $w1

        echo $n1|tr "\n" ",">>$path/${jifanghao}_close.txt
	echo $n2|tr "\n" ",">>$path/${jifanghao}_close.txt
        echo $w1>>$path/${jifanghao}_close.txt
	
fi

if [ ! -n "$k2" ]
        then
       	ip=`echo $LIST|cut -d ' ' -f 4`
	echo $ip
	n3=`echo $LIST | cut -d ' ' -f 10|cut -d '/' -f 4 ` #wenjianmingcheng
	p1=`echo $LIST | cut -d ' ' -f 10|cut -d '/' -f 2` 
        p2=`echo $LIST | cut -d ' ' -f 10|cut -d '/' -f 3`
        echo $n3
	jifanghao=`echo $n3|cut -b 20-24`
	echo $jifanghao
        w1=`wc -l /$p1/$p2/$n3` #wenjianhangshu
        echo $w1
	echo $ip|tr "\n" ",">>$path/${jifanghao}_rename.txt 
	echo $n3|tr "\n" "," >> $path/${jifanghao}_rename.txt
	echo $jifanghao >> $path/${jifanghao}_rename.txt
fi
