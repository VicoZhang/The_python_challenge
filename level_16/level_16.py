from datetime import datetime

for year in range(1006, 1996 + 1, 10):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        week = datetime.strptime("{}0101".format(year), "%Y%m%d").weekday()
        print(year, end=' ') if week == 3 else ...
