<script type="text/javascript">
        new Morris.Bar({
            element: 'daily_comments',
            data: [
              {% for comment in daily_comments %}
              { day: '{{ comment.day|date:"d-m-Y" }}', num_comments: {{ comment.num_comments }} },
              {% endfor %}
        ],
        xkey: 'day',
        ykeys: ['num_comments'],
        labels: ['Шарҳлар'],
        barColors: ['#2c3e50'],
        grid: true,
        axes: true,
        resize: true,
        gridTextColor: '#7f8c8d',
        gridTextSize: 10,
        gridTextFamily: 'Noto Serif',
        barRatio: 0.4,
        xLabelAngle: 45,
        hideHover: 'auto'
        });
        new Morris.Bar({
            element: 'monthly_comments',
            data: [
              {% for comment in monthly_comments %}
              { day: '{{ comment.month|date:"m-Y" }}', num_comments: {{ comment.num_comments }} },
              {% endfor %}
        ],
        xkey: 'day',
        ykeys: ['num_comments'],
        labels: ['Шарҳлар'],
        barColors: ['#2c3e50'],
        resize: true,
        gridTextColor: '#7f8c8d',
        gridTextSize: 10,
        gridTextFamily: 'Noto Serif',
        barRatio: 0.4,
        xLabelAngle: 45,
        hideHover: 'auto'
        });
        Morris.Donut({
        element: 'yearly_comments',
        data: [
          {% for comment in yearly_comments %}
          {label: '{{ comment.year|date:"Y" }} йил', value: {{ comment.num_comments }} },
          {% endfor %}
        ],
        colors: ['#2c3e50'],
        formatter: function(y, data) { return y + ' та шарҳ' },
        gridTextColor: '#7f8c8d',
        gridTextSize: 10,
        gridTextFamily: 'Noto Serif'
      });
</script>
