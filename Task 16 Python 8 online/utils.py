from datetime import datetime
import calendar
from itertools import chain

'''Function working_days returns list of days in month except weekends'''


def working_days(year, month):
    this_month = calendar.monthcalendar(year, month)
    days_passed_this_month = datetime.now().strftime('%d')
    work_days_list = list(chain.from_iterable(map(lambda date: date[0:5], this_month)))
    return [date for date in range(1, int(days_passed_this_month) + 1) if date in work_days_list]
