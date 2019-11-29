from datetime import datetime, timedelta, date
import os
import re

start_date = datetime(2019, 10, 1, 16, 15, 0)
end_date = datetime(2019, 10, 1, 16, 15, 0)
start_date2 = datetime(2019, 10, 2, 9, 30, 0)
end_date2 = datetime(2019, 10, 2, 16, 15, 0)
start_date3 = datetime(2019, 10, 1, 9, 30, 0)
end_date3 = datetime(2019, 10, 1, 16, 15, 0)
tdelta = timedelta(minutes=1)

ftitles2 = []
titles2 = []
ftitles = []
titles = []
i = 0
i2 = 0
i3 = 0

while start_date <= end_date:
    titles.append(str(start_date))
    filtered1 = re.sub(':', '', titles[i])
    filtered2 = re.sub(' ', '', filtered1)
    ftitles.append(filtered2)
    start_date = start_date + tdelta
    i += 1

while start_date3 <= end_date3:
    titles2.append(str(start_date3))
    filtered3 = re.sub(':', '', titles2[i3])
    filtered4 = re.sub(' ', '', filtered3)
    ftitles2.append(filtered4)
    start_date3 = start_date3 + tdelta
    i3 += 1

while start_date2 <= end_date2:
    filename = ftitles[i2] #+ ".png"
    filename2 = ftitles[i2] #+ "V.png"

    os.rename(filename, (ftitles2[i2] + ".png"))
    os.rename(filename2, (ftitles2[i2] + "V.png"))
    start_date2 = start_date2 + tdelta
    i2 += 1
