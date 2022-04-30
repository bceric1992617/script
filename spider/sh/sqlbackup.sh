#!/bin/bash

currentTime=`date +%Y%m%d`
LastTime=`date -v -1d +%Y%m%d`
# LastTime=`date -d last-day +%Y%m%d`

currentFileName="$currentTime.sql"
lastFileName="$LastTime.sql"
# echo $currentFileName
# echo $lastFileName
# exit;

/Applications/MAMP/Library/bin/mysqldump -hlocalhost -p8889 -uroot -p123321 --databases films2 > /Users/eric/Desktop/$currentFileName

if [ -f "/Users/eric/Desktop/$lastFileName" ];then
    rm -f /Users/eric/Desktop/$lastFileName
    echo "删除成功"
fi

