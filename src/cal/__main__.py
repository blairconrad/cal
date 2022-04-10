import datetime
import rich.console

import cal.builder


def main(*main_args):
    today = datetime.date.today()
    console = rich.console.Console(highlight=False, style="bold white")
    console.print("\n".join(cal.builder.format_month(today.year, today.month, today)))


if __name__ == "__main__":
    main()
