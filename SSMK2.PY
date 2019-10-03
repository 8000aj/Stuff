import mss
import mss.tools
import re
import cv2
import time
from pynput.mouse import Button, Controller
from datetime import datetime, timedelta, date

start_date = datetime(2019, 9, 27, 9, 30, 0)
end_date = datetime(2019, 9, 27, 16, 00, 0)
start_date2 = datetime(2019, 9, 27, 9, 30, 0)
end_date2 = datetime(2019, 9, 27, 16, 00, 0)
tdelta = timedelta(minutes=1)

mouse = Controller()

titles = []
ftitles = []
i = 0
i2 = 0


with mss.mss() as sct:
    while start_date <= end_date:
        titles.append(str(start_date))
        filtered1 = re.sub(':', '', titles[i])
        filtered2 = re.sub(' ', '', filtered1)
        ftitles.append(filtered2)
        start_date = start_date + tdelta
        i += 1

    while start_date2 <= end_date2:

        output = ftitles[i2] + ".png"
        output2 = ftitles[i2] + "V.png"

        # input("Press Enter // " + ftitles[i2])

        mouse.position = (662 + i2, 630)
        time.sleep(0.3)
        # perimeter of the screenshots
        monitor = {"top": 657, "left": 1226, "width": 144, "height": 98}
        monitor2 = {"top": 830, "left": 1226, "width": 144, "height": 34}

        # Grab the data
        # Save to the picture file

        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

        sct_img2 = sct.grab(monitor2)
        mss.tools.to_png(sct_img2.rgb, sct_img2.size, output=output2)

        print("path/to/" + output)
        print("path/to/" + output2)

        start_date2 = start_date2 + tdelta

        i2 += 1
