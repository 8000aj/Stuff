import mss
import mss.tools
import re
import cv2
import time
from pynput.mouse import Button, Controller
from datetime import datetime, timedelta, date

start_date = datetime(2019, 10, 2, 10, 34, 0)
end_date = datetime(2019, 10, 2, 16, 13, 0)
start_date2 = datetime(2019, 10, 2, 10, 34, 0)
end_date2 = datetime(2019, 10, 2, 16, 13, 0)
tdelta = timedelta(minutes=1)

mouse = Controller()

titles = []
ftitles = []
i = 0
i2 = 0


with mss.mss() as sct:
    # Iterates day by day
    while start_date <= end_date:
        # Uses datetime object to create a rough title
        # Filters out unnecessary characters
        # Stores in list
        titles.append(str(start_date))
        filtered1 = re.sub(':', '', titles[i])
        filtered2 = re.sub(' ', '', filtered1)
        ftitles.append(filtered2)
        start_date = start_date + tdelta
        i += 1

    while start_date2 <= end_date2:
        output = ftitles[i2] + ".png"
        output2 = ftitles[i2] + "V.png"

        # Manual / Auto toggle
        input("Press Enter // " + ftitles[i2])
        # mouse.position = (662 + i2, 630)
        # time.sleep(0.3)

        # perimeter of the screenshots
        monitor = {"top": 657, "left": 1226, "width": 144, "height": 98}
        monitor2 = {"top": 830, "left": 1226, "width": 144, "height": 34}

        # Grab the data
        # Save to the picture file
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

        sct_img2 = sct.grab(monitor2)
        mss.tools.to_png(sct_img2.rgb, sct_img2.size, output=output2)

        # Prints data for Tesseract title list
        print("path/to/" + output)
        print("path/to/" + output2)

        start_date2 = start_date2 + tdelta

        i2 += 1
