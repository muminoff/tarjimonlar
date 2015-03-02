#!/bin/bash

set -e

./manage.py posts_chart >./static/js/posts_chart.js
./manage.py comments_chart >./static/js/comments_chart.js
