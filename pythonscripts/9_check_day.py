
import datetime
import csv

with open("timestamps.csv","r") as csvfile:

    month = {"Apr":"April","Mar":"March","May":"May"}
    weekday_count = {"Sunday":0,'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0}
    reader = csv.reader(csvfile)
    weekend = weekday = total_count = 0
    for row in reader:
        day = datetime.datetime.strptime(month[row[0][0:3]] + str(row[0][3:6])+' 2015', '%B %d %Y').strftime('%A')
        if day == ("Friday" or "Saturday" or "Sunday"):
            weekend += int(row[1])
            weekday_count[day] += 1
        else:
            weekday += int(row[1])
            weekday_count[day] += 1
        total_count += int(row[1])

    print('weekend:',weekend,'weekday:',weekday, 'totalcount:', total_count)
    print(weekday_count)
