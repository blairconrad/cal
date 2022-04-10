import calendar


def print_month(year, month):
    calendar.setfirstweekday(calendar.SUNDAY)
    heading = calendar.month_name[month] + " " + str(year)
    print(heading.center(20))
    print(calendar.weekheader(2))

    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    for week in c.monthdatescalendar(year, month):
        cell_values = []
        for day in week:
            if day.month == month:
                cell_values.append(f"{day.day:2}")
            else:
                cell_values.append("  ")
        print(" ".join(cell_values))
