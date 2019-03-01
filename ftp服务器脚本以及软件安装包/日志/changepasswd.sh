#!/usr/bin/expect
set i 1
while {$i < 65} {
set HOST 10.0.9.$i
spawn ssh root@$HOST
set timeout 3
sleep 0.2
send "root_China1120!@#$\r"
sleep 0.2
send "*&idcisp_Unicom4567!@#$\r"
sleep 0.2
send "*&idcisp_Unicom4567!@#$\r"
sleep 0.2

incr i
}