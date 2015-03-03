#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

echo 'Start' `date` >/tmp/last_time
/home/ubuntu/tarjimonlar/manage.py import_members
/home/ubuntu/tarjimonlar/manage.py import_posts
/home/ubuntu/tarjimonlar/manage.py import_comments
/home/ubuntu/tarjimonlar/manage.py update_index core
/home/ubuntu/tarjimonlar/manage.py posts_chart >/home/ubuntu/tarjimonlar/static/js/posts_chart.js
/home/ubuntu/tarjimonlar/manage.py comments_chart >/home/ubuntu/tarjimonlar/static/js/comments_chart.js
rm -rf /home/ubuntu/staticfiles
/home/ubuntu/tarjimonlar/manage.py collectstatic --noinput
/usr/bin/redis-cli -n 1 flushdb
echo 'Finish' `date` >>/tmp/last_time
