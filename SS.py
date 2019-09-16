# screencaps day minute data & titles each picture correctly
# {930 - 249]
import pyscreenshot as ImageGrab
from PIL import Image, ImageOps
from datetime import datetime, timedelta, date
import re
from pynput.mouse import Button, Controller

if __name__ == '__main__':

    mouse = Controller()

    start_date = datetime(2019, 9, 13, 9, 30, 0)
    end_date = datetime(2019, 9, 13, 16, 00, 0)

    tdelta = timedelta(minutes=1)

    titles = []
    ftitles = []
    i = 0

    while start_date <= end_date:

        titles.append(str(start_date))
        filtered1 = re.sub(':', '', titles[i])
        filtered2 = re.sub(' ', '', filtered1)
        filtered3 = re.sub('-', '', filtered2)
        ftitles.append(filtered2)
        start_date = start_date + tdelta

        # grab part of the screen
        im = ImageGrab.grab(bbox=(1226, 657, 1370, 755))  # X1,Y1,X2,Y2
        im2 = ImageGrab.grab(bbox=(1226, 829, 1370, 864))
        # invert colours(improves accuracy in Tesseract 4)
        inverted = ImageOps.invert(im)
        inverted2 = ImageOps.invert(im2)
        # title statements
        inverted.save(filtered2 + '.png')
        inverted2.save(filtered2 + 'V' + '.png')

        # moves mouse to 9:30, then iterates till 4:00
        mouse.position = (661.5 + i, 672)
        # print(mouse.position)
        print(ftitles[i])
        print(ftitles[i] + "V")

        i += 1
