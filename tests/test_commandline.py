import cal.__main__


def test_no_args_prints_current_month(capsys):
    expected = """\
     April 2022     
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
"""  # noqa - don't check trailing whitespace in multiline string
    run_cal()
    (actual_output, actual_error) = capsys.readouterr()
    assert actual_output == expected


def run_cal(*extra_args: str) -> None:
    cal.__main__.main(*extra_args)
