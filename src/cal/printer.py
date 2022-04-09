import calendar


def print(year, month):
    calendar.TextCalendar(firstweekday=calendar.SUNDAY).prmonth(year, month)
