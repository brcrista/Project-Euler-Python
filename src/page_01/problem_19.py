from enum import IntEnum

from mathtools.number_theory import divides

class Day(IntEnum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

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

def day_mod(day: Day, days_elapsed: int) -> Day:
    return Day((day + days_elapsed) % 7)

def count_sundays_on_first_of_month() -> int:
    day_of_week = day_mod(Day.MONDAY, 365) # Jan 1 1900 was a Monday -- but we are starting in 1901!
    total_sundays_on_first_of_month = 0
    for year in range(1901, 2001):
        for month, days_in_month in months.items():
            if is_leap_year(year) and month == 'February':
                day_of_week = day_mod(day_of_week, 29)
            else:
                day_of_week = day_mod(day_of_week, days_in_month)
            if day_of_week == Day.SUNDAY:
                total_sundays_on_first_of_month += 1
    return total_sundays_on_first_of_month

solution = count_sundays_on_first_of_month
