import calendar
year=2024
month= 11 #November
print(calendar.month(year,month))
print(calendar.calendar(year))
is_leap = calendar.isleap(year)
print(f'{year} is a leap year: {is_leap}')
weekday_index= calendar.weekday(2025,1,1)
print(f"January 1,2025 is a weekday index: {weekday_index}")

