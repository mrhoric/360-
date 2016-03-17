#!/bin/bash

LOGPATH="/var/log/access.log"
SAVEPATH="/var/log/"
PIDPATH="/var/run/nginx.pid"

mv $LOGPATH $SAVEPATH`date '+%Y-%m-%d' --date="-1 day"`.log
touch $LOGPATH

kill -HUP `cat $PIDPATH`
