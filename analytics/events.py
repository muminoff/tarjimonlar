from datetime import datetime, timedelta
from bitmapist import setup_redis, delete_all_events,\
        mark_event, MonthEvents, WeekEvents,\
        DayEvents, HourEvents, BitOpAnd, BitOpOr


def user_loggedin_event(userid
