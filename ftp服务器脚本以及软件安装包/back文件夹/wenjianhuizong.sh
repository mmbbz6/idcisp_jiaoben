#!/bin/bash
date=$1

for i in {1..64}
do
ip=10.0.108.$i
ssh root@$ip "cat /ftpdata/log2/${date}.log;">> /ftpdata/log2/${date}.log;
done


for i in {1..59}
do
ip=10.0.109.$i
ssh root@$ip "cat /ftpdata/log2/${date}.log;">> /ftpdata/log2/${date}.log;
done