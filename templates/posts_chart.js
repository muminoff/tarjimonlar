{% load localize_time %}
        new Morris.Bar({
            element: 'daily_posts',
            data: [
              {% for post in daily_posts %}
              { day: '{{ post.day|date:"d-m-Y"|uzbekify_daymonthyear }}', num_posts: {{ post.num_posts }} },
              {% endfor %}
        ],
        xkey: 'day',
        ykeys: ['num_posts'],
        labels: ['Постлар'],
        barColors: ['#2c3e50'],
        grid: true,
        axes: true,
        resize: true,
        gridTextColor: '#7f8c8d',
        gridTextSize: 10,
        gridTextFamily: 'Noto Serif',
        barRatio: 0.4,
        xLabelAngle: 0,
        hideHover: 'auto'
        });
        new Morris.Bar({
            element: 'monthly_posts',
            data: [
              {% for post in monthly_posts %}
              { day: '{{ post.month|date:"m-Y"|uzbekify_monthyear|capfirst }}', num_posts: {{ post.num_posts }} },
              {% endfor %}
        ],
        xkey: 'day',
        ykeys: ['num_posts'],
        labels: ['Постлар'],
        barColors: ['#16a085'],
        resize: true,
        gridTextColor: '#7f8c8d',
        gridTextSize: 10,
        gridTextFamily: 'Noto Serif',
        barRatio: 0.4,
        xLabelAngle: 15,
        hideHover: 'auto'
        });
        Morris.Donut({
        element: 'yearly_posts',
        data: [
          {% for post in yearly_posts %}
          {label: '{{ post.year|date:"Y" }} йилда', value: {{ post.num_posts }} },
          {% endfor %}
        ],
        colors: ['#2c3e50', '#c0392b', '#2980b9'],
        formatter: function(y, data) { return y + ' та пост' },
        gridTextColor: '#7f8c8d',
        gridTextSize: 10,
        gridTextFamily: 'Noto Serif'
      });
