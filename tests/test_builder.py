import datetime

import cal.builder


def test_format_month_today_in_month_highlighted():
    expected = """\
     April 2022     
Su Mo Tu We Th Fr Sa
[bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2
 3  4  5  6  7  8 [bold cyan] 9[/bold cyan]
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30"""  # noqa - don't check trailing whitespace in multiline string

    actual = "\n".join(cal.builder.format_month(2022, 4, datetime.date(2022, 4, 9)))
    assert actual == expected


def test_format_month_today_not_in_month_not_highlighted():
    expected = """\
     April 2022     
Su Mo Tu We Th Fr Sa
[bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30"""  # noqa - don't check trailing whitespace in multiline string

    actual = "\n".join(cal.builder.format_month(2022, 4, datetime.date(2023, 4, 9)))
    assert actual == expected


def test_format_three_months_today_in_month_highlighted():
    expected = """\
     March 2022             April 2022              May 2022      
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
[bold black]27[/bold black] [bold black]28[/bold black]  1  2  3  4  5   [bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2    1  2  3  4  5  6  7
 6  7  8  9 10 11 12    3  4  5  6  7  8 [bold cyan] 9[/bold cyan]    8  9 10 11 12 13 14
13 14 15 16 17 18 19   10 11 12 13 14 15 16   15 16 17 18 19 20 21
20 21 22 23 24 25 26   17 18 19 20 21 22 23   22 23 24 25 26 27 28
27 28 29 30 31 [bold black] 1[/bold black] [bold black] 2[/bold black]   24 25 26 27 28 29 30   29 30 31 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black] [bold black] 4[/bold black]"""  # noqa - don't check trailing whitespace in multiline string

    actual = "\n".join(cal.builder.format_three_months(2022, 3, datetime.date(2022, 4, 9)))
    assert actual == expected


def test_format_three_months_today_not_in_month_not_highlighted():
    expected = """\
     April 2022              May 2022              June 2022      
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
[bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2    1  2  3  4  5  6  7   [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2  3  4
 3  4  5  6  7  8  9    8  9 10 11 12 13 14    5  6  7  8  9 10 11
10 11 12 13 14 15 16   15 16 17 18 19 20 21   12 13 14 15 16 17 18
17 18 19 20 21 22 23   22 23 24 25 26 27 28   19 20 21 22 23 24 25
24 25 26 27 28 29 30   29 30 31 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black] [bold black] 4[/bold black]   26 27 28 29 30 [bold black] 1[/bold black] [bold black] 2[/bold black]"""  # noqa - don't check trailing whitespace in multiline string

    actual = "\n".join(cal.builder.format_three_months(2022, 4, datetime.date(2023, 4, 9)))
    assert actual == expected


def test_format_three_months_with_different_lengths():
    expected = """\
      May 2022              June 2022              July 2022      
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7   [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2  3  4   [bold black]26[/bold black] [bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black]  1  2
 8  9 10 11 12 13 14    5  6  7  8  9 10 11    3  4  5  6  7  8  9
15 16 17 18 19 20 21   12 13 14 15 16 17 18   10 11 12 13 14 15 16
22 23 24 25 26 27 28   19 20 21 22 23 24 25   17 18 19 20 21 22 23
29 30 31 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black] [bold black] 4[/bold black]   26 27 28 29 30 [bold black] 1[/bold black] [bold black] 2[/bold black]   24 25 26 27 28 29 30
                                              31 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black] [bold black] 4[/bold black] [bold black] 5[/bold black] [bold black] 6[/bold black]"""  # noqa - don't check trailing whitespace in multiline string
    actual = "\n".join(cal.builder.format_three_months(2022, 5, datetime.date(2023, 4, 9)))
    assert actual == expected


def test_format_year_today_in_year_today_not_highlighted():
    expected = """\
    January 2022          February 2022            March 2022     
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
[bold black]26[/bold black] [bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1   [bold black]30[/bold black] [bold black]31[/bold black]  1  2  3  4  5   [bold black]27[/bold black] [bold black]28[/bold black]  1  2  3  4  5
 2  3  4  5  6  7  8    6  7  8  9 10 11 12    6  7  8  9 10 11 12
 9 10 11 12 13 14 15   13 14 15 16 17 18 19   13 14 15 16 17 18 19
16 17 18 19 20 21 22   20 21 22 23 24 25 26   20 21 22 23 24 25 26
23 24 25 26 27 28 29   27 28 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black] [bold black] 4[/bold black] [bold black] 5[/bold black]   27 28 29 30 31 [bold black] 1[/bold black] [bold black] 2[/bold black]
30 31 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black] [bold black] 4[/bold black] [bold black] 5[/bold black]                                              

     April 2022              May 2022              June 2022      
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
[bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2    1  2  3  4  5  6  7   [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2  3  4
 3  4  5  6  7  8  9    8  9 10 11 12 13 14    5  6  7  8  9 10 11
10 [bold cyan]11[/bold cyan] 12 13 14 15 16   15 16 17 18 19 20 21   12 13 14 15 16 17 18
17 18 19 20 21 22 23   22 23 24 25 26 27 28   19 20 21 22 23 24 25
24 25 26 27 28 29 30   29 30 31 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black] [bold black] 4[/bold black]   26 27 28 29 30 [bold black] 1[/bold black] [bold black] 2[/bold black]

     July 2022             August 2022           September 2022   
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
[bold black]26[/bold black] [bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black]  1  2   [bold black]31[/bold black]  1  2  3  4  5  6   [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black] [bold black]31[/bold black]  1  2  3
 3  4  5  6  7  8  9    7  8  9 10 11 12 13    4  5  6  7  8  9 10
10 11 12 13 14 15 16   14 15 16 17 18 19 20   11 12 13 14 15 16 17
17 18 19 20 21 22 23   21 22 23 24 25 26 27   18 19 20 21 22 23 24
24 25 26 27 28 29 30   28 29 30 31 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black]   25 26 27 28 29 30 [bold black] 1[/bold black]
31 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black] [bold black] 4[/bold black] [bold black] 5[/bold black] [bold black] 6[/bold black]                                              

    October 2022          November 2022          December 2022    
Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa   Su Mo Tu We Th Fr Sa
[bold black]25[/bold black] [bold black]26[/bold black] [bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black]  1   [bold black]30[/bold black] [bold black]31[/bold black]  1  2  3  4  5   [bold black]27[/bold black] [bold black]28[/bold black] [bold black]29[/bold black] [bold black]30[/bold black]  1  2  3
 2  3  4  5  6  7  8    6  7  8  9 10 11 12    4  5  6  7  8  9 10
 9 10 11 12 13 14 15   13 14 15 16 17 18 19   11 12 13 14 15 16 17
16 17 18 19 20 21 22   20 21 22 23 24 25 26   18 19 20 21 22 23 24
23 24 25 26 27 28 29   27 28 29 30 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black]   25 26 27 28 29 30 31
30 31 [bold black] 1[/bold black] [bold black] 2[/bold black] [bold black] 3[/bold black] [bold black] 4[/bold black] [bold black] 5[/bold black]                                              """  # noqa - don't check trailing whitespace in multiline string
    actual = "\n".join(cal.builder.format_year(2022, datetime.date(2022, 4, 11)))
    assert actual == expected
