"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from enum import IntEnum
from typing import Iterator

from mathtools.number_theory import divides

class Day(IntEnum):
    """
    The integer values of this enum match with the values used by the `calendar` module:
    https://docs.python.org/3/library/calendar.html.
    """
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

months = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

def is_leap_year(year: int) -> bool:
    return divides(year, 4) and (divides(year, 400) or not divides(year, 100))

def days_in_year(year: int) -> int:
    return 366 if is_leap_year(year) else 365

def day_mod(day: Day, days_elapsed: int) -> Day:
    """The day of the week `days_elapsed` after `day`."""
    return Day((day + days_elapsed) % 7)

def first_day_of_each_month() -> Iterator[Day]:
    day_of_week = day_mod(Day.MONDAY, days_in_year(1900)) # 1 Jan 1900 was a Monday -- but we are starting in 1901!
    yield day_of_week
    for year in range(1901, 2001):
        for month, days_in_month in months.items():
            if is_leap_year(year) and month == 'February':
                days_in_month = 29
            day_of_week = day_mod(day_of_week, days_in_month)
            yield day_of_week

def count_sundays_on_first_of_month() -> int:
    return len([day for day in first_day_of_each_month() if day == Day.SUNDAY])

solution = count_sundays_on_first_of_month
