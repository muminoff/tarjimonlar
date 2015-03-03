#!/bin/bash

# set -e

rm ./static/js/comments_chart.js
rm ./static/js/posts_chart.js

git pull origin develop
killall gunicorn

./manage.py posts_chart >./static/js/posts_chart.js
./manage.py comments_chart >./static/js/comments_chart.js

rm -rf ../staticfiles

./manage.py collectstatic --noinput >/dev/null

nohup gunicorn deploy.wsgi:application --workers 4 --worker-class gevent &
echo "Cleaning cache"
redis-cli -n 1 flushdb >/dev/null
