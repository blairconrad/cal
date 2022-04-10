import cal.printer


def test_today_highlighted_in_month():
    expected = """\
     April 2022     
Su Mo Tu We Th Fr Sa
[bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2
 3  4  5  6  7  8 [bold cyan] 9[/bold cyan]
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30"""  # noqa - don't check trailing whitespace in multiline string

    actual = "\n".join(cal.printer.format_month(2022, 4, 9))
    assert actual == expected


def test_no_today_not_highlighted_in_month():
    expected = """\
     April 2022     
Su Mo Tu We Th Fr Sa
[bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30"""  # noqa - don't check trailing whitespace in multiline string

    actual = "\n".join(cal.printer.format_month(2022, 4))
    assert actual == expected
