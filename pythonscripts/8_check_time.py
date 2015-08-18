import datetime
import csv

with open("timestamps.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    day_count = night_count = total_count = 0
    for row in reader:
        timestamp = row[0]
        if 8 <= int(timestamp[7:9]) <= 16:
            day_count += int(row[1])
        else:
            night_count += int(row[1])

        total_count += int(row[1])
    print('day count:',day_count,'night count:', night_count, 'total_count',total_count)

