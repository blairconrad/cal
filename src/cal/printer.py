import calendar
import rich.console


def format_month(year, month, today=None):
    calendar.setfirstweekday(calendar.SUNDAY)
    month_header = calendar.month_name[month] + " " + str(year)

    yield month_header.center(20)
    yield calendar.weekheader(2)

    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    for week in c.monthdatescalendar(year, month):
        cell_values = []
        for day in week:
            if day.month == month:
                value = f"{day.day:2}"
                if day.day == today:
                    value = f"[bold cyan]{value}[/bold cyan]"
                cell_values.append(value)
            else:
                cell_values.append("  ")
        yield " ".join(cell_values)


def print_month(year, month, today=None):
    console = rich.console.Console(highlight=False)
    console.print("\n".join(format_month(year, month, today)))
