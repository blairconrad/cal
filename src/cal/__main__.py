import datetime

import cal.printer


def main(*main_args):
    now = datetime.date.today()
    cal.printer.print_month(now.year, now.month, now.day)


if __name__ == "__main__":
    main()
