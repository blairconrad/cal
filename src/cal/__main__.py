import datetime
import rich.console

import cal.builder


def main(*main_args):
    now = datetime.date.today()
    console = rich.console.Console(highlight=False, style="bold white")
    console.print("\n".join(cal.builder.format_month(now.year, now.month, now.today)))


if __name__ == "__main__":
    main()
