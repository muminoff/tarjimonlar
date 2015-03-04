#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

import_data_from_facebook() {
	/home/ubuntu/tarjimonlar/manage.py import_members
	/home/ubuntu/tarjimonlar/manage.py import_posts
	/home/ubuntu/tarjimonlar/manage.py import_comments
}
update_search_index() {
	/home/ubuntu/tarjimonlar/manage.py update_index core
}
build_assets() {
	/home/ubuntu/tarjimonlar/manage.py posts_chart >/home/ubuntu/tarjimonlar/static/js/posts_chart.js
	/home/ubuntu/tarjimonlar/manage.py comments_chart >/home/ubuntu/tarjimonlar/static/js/comments_chart.js
	/home/ubuntu/tarjimonlar/manage.py collectstatic --noinput >/tmp/collecstatic`date`
}
clear_cache() {
	echo "Cache clear..."
	/usr/bin/redis-cli -n 1 flushdb
}
echo 'Start' `date +"%y%m%d%H%M"` >/tmp/last_time
build_assets && clear_cache >>/tmp/last_time
echo 'Finish' `date "%y%m%d%H%M"` >>/tmp/last_time
