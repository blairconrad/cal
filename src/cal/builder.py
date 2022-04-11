import calendar
import datetime
import itertools


def format_year(year, today):
    lines = []
    for month in range(1, 13, 3):
        if month != 1:
            lines.append("")
        lines += format_three_months(year, month, today)
    return lines


def format_three_months(year, month, today):
    next_month = (datetime.date(year, month, 1) + datetime.timedelta(days=32)).replace(day=1)
    next_next_month = (next_month + datetime.timedelta(days=32)).replace(day=1)

    this_month_lines = format_month(year, month, today)
    next_month_lines = format_month(next_month.year, next_month.month, today)
    next_next_month_lines = format_month(next_next_month.year, next_next_month.month, today)

    return [
        "   ".join(t)
        for t in (itertools.zip_longest(this_month_lines, next_month_lines, next_next_month_lines, fillvalue=20 * " "))
    ]


def format_month(year, month, today):
    calendar.setfirstweekday(calendar.SUNDAY)
    month_header = calendar.month_name[month] + " " + str(year)

    yield month_header.center(20)
    yield calendar.weekheader(2)

    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    for week in c.monthdatescalendar(year, month):
        cell_values = []
        for day in week:
            value = f"{day.day:2}"
            if day.month == month:
                if day == today:
                    value = f"[bold red]{value}[/bold red]"
            else:
                value = f"[bold black]{value}[/bold black]"

            cell_values.append(value)
        yield " ".join(cell_values)
