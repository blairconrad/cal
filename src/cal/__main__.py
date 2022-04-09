import datetime

import cal.printer


def main(*main_args):
    now = datetime.date.today()
    cal.printer.print(now.year, now.month)


if __name__ == "__main__":
    main()
