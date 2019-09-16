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
filename = "C:/Users/AJ/Desktop/SS1/SPY2019-08-28/output_spy20190828.txt"

# lots of reassignments... perhaps a rewrite is simpler? one list.
list = []
flist = []
fflist = []
ffflist = []
fffflist = []
ffffflist = []

daydate = []
daytime = []
open_price = []
high_price = []
low_price = []
close_price = []
volume = []
volume2 = []


with open(filename) as f:

    def EmptyValue(x):
        if x == '':
            return False
        else:
            return True

    # filters .txt fragments, then migrates data to list
    for line in f:
        filtered1 = re.sub('\n', '', line)
        filtered2 = re.sub('\x0c', '', filtered1)
        filtered3 = re.sub(',', '', filtered2)
        list.append(filtered3)

    # filters all empty lines
    flist = (filter(EmptyValue, list))

    # migrates from flist to fflist, from filter objects to string objects.
    for line in flist:
        fflist.append(str(line))

    # rejoins seperated data
    i = 0
    while i < len(fflist):

        if (fflist[i] == "Open") or (fflist[i] == "High") or (fflist[i] == "Low") or (fflist[i] == "Close"):
            ffflist.append(fflist[i] + " " + fflist[4 + i])
        elif (len(fflist[i]) == 5) or (len(fflist[i]) == 6):
            None
        else:
            ffflist.append(fflist[i])
        i += 1

    # filtering the daydate & daytime above the volume cells
    y = 0
    while y < len(ffflist):
        if y in range(5, 2739, 7):
            pass
        else:
            fffflist.append(ffflist[y])
        y += 1

    # divides data into independent lists

    for l in fffflist:
        if len(l) >= 19:
            ffffflist.append(l[:19])
        else:
            ffffflist.append(l)

    for l in ffffflist:
        if l[:4] == "2019":
            daydate.append(l[:10])
            daytime.append(l[11:19])
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

    for l in volume:
        if "M" in l:
            volume2.append(int((float(l[:-1])) * 1000000))
        else:
            volume2.append(int(float(l)))

    try:
        for x in range(0, 391, 1):
            with con.cursor() as cursor:
                # Create a new record
                val = ((str(daydate[x])), (str(daytime[x])), (str(open_price[x])), (str(high_price[x])), (str(low_price[x])), (str(close_price[x])), (str(volume2[x])))
                sql = "INSERT INTO `spy20190828` (`daydate`, `daytime`, `open_price`, `high_price`, `low_price`, `close_price`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(sql, val)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
                con.commit()
            cur.execute("SELECT * FROM spy.spy20190828")

    finally:
        con.close()

    for l in daydate, daytime, open_price, high_price, low_price, close_price, volume2:
        print(l)

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
