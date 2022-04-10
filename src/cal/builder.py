import calendar


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
                    value = f"[bold cyan]{value}[/bold cyan]"
            else:
                value = f"[bold black]{value}[/bold black]"

            cell_values.append(value)
        yield " ".join(cell_values)
