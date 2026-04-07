import datetime as dt
now = dt.datetime.now()
year = now.year

date_of_birth = dt.datetime(year=2003, month=2, day=13)
print(date_of_birth)


if year == 2026:
    print(f"Years is {year}")
