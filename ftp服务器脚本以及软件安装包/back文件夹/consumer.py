#!/usr/bin/python
# _*_ coding:utf-8 _*_

from pykafka import KafkaClient
import json
import ast
import re
import os
import time
from threading import Timer
import sched
import datetime
import threading
import threadpool
import pdb

lock = threading.Lock()
def fun(d):
        for k, v in d.items():
                with open(k, 'a+') as f:
                        for i in range(0,len(v)):
                                f.write('%s %s %s %s %s %s\n' % (v[i][0],v[i][1],v[i][2], v[i][3], v[i][4], v[i][5]) )

        d.clear()
        balanced_consumer.commit_offsets()





def fun2(l1):
        global lock
        rows = 0
        numflag=1
        d = {}
        s1=1

        for message in balanced_consumer:
                numflag=1
                if s1 == 1:
                        starttime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                        s1 = 0

                if message is not None:
                        msg=message.value
                        msg2=ast.literal_eval(msg)
                        msg3 = msg2.get('message')
                        msg4 = re.split(r'[\s]+', msg3)

                        endwith=re.compile(r'.*.gz') 
                        if endwith.match(msg4[2]):
                                flag = 'idcisp-rename'
                        else:
                                flag = 'idcisp-close'

                        path = '/ftpdata/log/'
                        if not os.path.exists(path):
                                os.makedirs(path)

                        path2 = path + msg4[5] + '/'  
                        if not os.path.exists(path2):
                                os.makedirs(path2)

                        filenamepath = path2 +  msg4[4][0:10] + '_' + flag + '.txt'
                        if not filenamepath in d:
                                v = ((msg4[0],msg4[1],msg4[2],msg4[3],msg4[4],msg4[5]),)
                                d[filenamepath] = v
                        else:
                                v0 = d[filenamepath]
                                v1 = ((msg4[0],msg4[1],msg4[2],msg4[3],msg4[4],msg4[5]),)
                                d[filenamepath] = v0 + v1
                        rows += 1
                        if rows == 200:
                                if lock.acquire():
                                        try:
                                                fun(d)
                                        except:
                                                pass
                                        finally:
                                                lock.release()
                                                rows=0
                                                s1=1
                                                numflag=0



                endtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                duration = int(endtime) - int(starttime)
                if duration >= 6 and numflag==1:
                        if lock.acquire():
                                try:
                                        fun(d)
                                        s1=1
                                except:
                                        pass
                                finally:
                                        lock.release()
                                        rows=0




if __name__ == '__main__':
        client=KafkaClient(hosts='10.0.8.51:9092')
        topic=client.topics['kafka_ftp']


        balanced_consumer = topic.get_balanced_consumer(
        reset_offset_on_start=False,
        consumer_group='testgroup',
        auto_commit_enable=False,
        auto_commit_interval_ms=1000000,
        zookeeper_connect='10.0.8.51:2181'
        )
        pool = threadpool.ThreadPool(10)
        l1=[1,2,3,4,5,6,7,8,9,10]
        tasks = threadpool.makeRequests(fun2, l1)
        [pool.putRequest(task) for task in tasks]
        pool.wait()