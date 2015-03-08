#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

update_search_index() {
	/home/ubuntu/tarjimonlar/manage.py update_index core
}

echo 'Start' `date +"%y%m%d%H%M"` >/tmp/last_time_index
update_search_index >>/tmp/last_time_index
echo 'Finish' `date +"%y%m%d%H%M"` >>/tmp/last_time_index
