#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

import_data_from_facebook() {
	/home/ubuntu/tarjimonlar/manage.py import_members
 	/home/ubuntu/tarjimonlar/manage.py import_posts
 	/home/ubuntu/tarjimonlar/manage.py import_comments
}
build_assets() {
	/home/ubuntu/tarjimonlar/manage.py posts_chart >/home/ubuntu/tarjimonlar/static/js/posts_chart.js
	/home/ubuntu/tarjimonlar/manage.py comments_chart >/home/ubuntu/tarjimonlar/static/js/comments_chart.js
	/home/ubuntu/tarjimonlar/manage.py collectstatic --noinput
	redis-client -n 1 flushdb
}
echo 'Start' `date +"%y%m%d%H%M"` >/tmp/last_time_import
import_data_from_facebook >>/tmp/last_time_import
build_assets >>/tmp/last_time_import
echo 'Finish' `date +"%y%m%d%H%M"` >>/tmp/last_time_import
