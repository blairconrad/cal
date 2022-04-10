import datetime
import rich.console

import cal.builder


def main(*main_args):
    today = datetime.date.today()
    console = rich.console.Console(highlight=False, style="bold white")

    for line in cal.builder.format_three_months(today.year, today.month, today):
        console.print(line)


if __name__ == "__main__":
    main()
