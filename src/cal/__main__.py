"""\
Print a calendar. By default prints the next 3 months, but this can be changed.
"""
import argparse
import datetime
import rich.console

import cal.builder


def main():
    today = datetime.date.today()
    console = rich.console.Console(highlight=False, style="bold white")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("year", type=int, nargs="?", help="The year of the calendar to print.")
    args = parser.parse_args()

    if args.year is None:
        for line in cal.builder.format_three_months(today.year, today.month, today):
            console.print(line)
    else:
        for line in cal.builder.format_year(args.year, today):
            console.print(line)


if __name__ == "__main__":
    main()
