def is_leap_year(year):
    """Checks whether a year is leap or not"""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

result = is_leap_year(1700)
print(result)