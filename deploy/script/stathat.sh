#!/bin/bash

set -e

loadavg=`head -c 4 /proc/loadavg`
freemem=`cat /proc/meminfo |head -n 2|awk '{print $2 }'|xargs|awk '{print $2}'`
curl -d "stat=load average&ezkey=dev@tarjimonlar.org&value=$loadavg" http://api.stathat.com/ez
curl -d "stat=free memory&ezkey=dev@tarjimonlar.org&value=$freemem" http://api.stathat.com/ez
echo $loadavg $freemem `date` >/tmp/loadavg
