import re
from datetime import datetime, timedelta, date
import pymysql.cursors

con = pymysql.connect(host="localhost",
                      user="jefferson",
                      passwd="1234",
                      db="spy"
                      )
cur = con.cursor()


start_date = datetime(2019, 7, 31, 9, 30, 0)
end_date = datetime(2019, 7, 31, 16, 00, 0)

# directs filename
filename = "output100.txt"
# set up the lists
list = []
flist = []
fflist = []
ffflist = []
fffflist = []

daydate = []
daytime = []
open_price = []
high_price = []
low_price = []
close_price = []
volume = []


# FILTERING
# filter removes \n, \x0c, x from the txt file
# filter removes empty strings // EmptyValue
with open(filename) as f:

    def EmptyValue(x):
        if x == '':
            return False
        else:
            return True

    for line in f:
        filtered1 = re.sub('\n', '', line)
        filtered2 = re.sub('\x0c', '', filtered1)
        list.append(filtered2)

    flist = (filter(EmptyValue, list))

    for line in flist:
        fflist.append(str(line))

    i = 0
    while i < len(fflist):
        # print(len(fflist[i]))

        if len(fflist[i]) <= 5:
            ffflist.append(fflist[i] + " " + fflist[4 + i])

        elif len(fflist[i]) == 6:
            None

        else:
            ffflist.append(fflist[i])
        i += 1

    x = 0
    while x < len(ffflist):
        if x in range(5, 2737, 7):
            None
        else:
            fffflist.append(ffflist[x])
        x += 1

    for l in fffflist:

        if l[:4] == "2019":
            daydate.append(l[:10])
            daytime.append(l[-9:19])
        if l[:4] == "Open":
            open_price.append(l[-6:])
        if l[:4] == "High":
            high_price.append(l[-6:])
        if l[:3] == "Low":
            low_price.append(l[-6:])
        if l[:5] == "Close":
            close_price.append(l[-6:])
        if l[:6] == "Volume":
            volume.append(l[7:])

    for x in range(0, len(daydate), 1):

        with con.cursor() as cursor:
            # Create a new record
            val = ((str(daydate[x])), (str(daytime[x])), (str(open_price[x])), (str(high_price[x])), (str(low_price[x])), (str(close_price[x])), (str(volume[x])))
            sql = "INSERT INTO `spy20190731` (`DAYDATE`, `daytime`, `OPEN_PRICE`, `HIGH_PRICE`, `LOW_PRICE`, `CLOSE_PRICE`, `VOLUME`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, val)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
            con.commit()

    cur.execute("SELECT * FROM spy.spy20190731")

    for row in cur:
        print(row)

    con.close()

    # n = 0
    # tdelta = timedelta(minutes=n)

    # date_string = '2019-07-31 09:30 AM'
    # format = '%Y-%m-%d %I:%M %p'
    # my_date1 = (datetime.strptime(date_string, format) + tdelta).strftime(format)
    # my_date2 = my_date1 + " x"
    # print(my_date2) = 2019-07-31 09:30 AM X

    # 2/7 "open" followed by a float

    #   if len(m) == 4:
    # perform rearrangement and continue
    #        print(n)

    # while start_date <= end_date:
    #    print(start_date)

    #    start_date = start_date + tdelta

    # for x in flist:
    #    print(x)

    #
    # for line in lines:
    #    if re.match("2019-07-31 09:30 A", line):
    #        print(line)
