import cv2
import pyscreenshot as ImageGrab
from PIL import Image, ImageOps
from datetime import datetime, timedelta, date
from pylab import array, plot, show, axis, arange, figure, uint8
from pynput.mouse import Button, Controller
import re
# pic = "C:/Users/AJ/Desktop/newImage0.jpg"

# img = cv2.imread(pic, 0)

# imagem = cv2.bitwise_not(img)

# cv2.imshow('imagem', imagem)
# cv2.waitKey()

# cv2.imwrite('imagem.png', imagem)
#  ///

# pic = "C:/Users/AJ/Desktop/SS1/test/2019-09-16093000.png"
# im = ImageGrab.grab(bbox=(1226, 657, 1370, 755))
# img1 = cv2.imread(pic)
# cv2.imshow('test', img1)
# cv2.waitKey()

# ///
if __name__ == '__main__':

    start_date = datetime(2019, 9, 27, 9, 30, 0)
    end_date = datetime(2019, 9, 27, 16, 00, 0)
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

        # # moves mouse to 9:30, then iterates till 4:00
        # mouse.position = (662.5 + i, 672)
        # # grab part of the screen
        # im = ImageGrab.grab(bbox=(1226, 657, 1370, 755))  # X1,Y1,X2,Y2
        # im2 = ImageGrab.grab(bbox=(1226, 829, 1370, 864))

        pic = "C:/Users/AJ/Desktop/SS1/Part One/" + ftitles[i] + ".png"
        pic2 = "C:/Users/AJ/Desktop/SS1/Part One/" + ftitles[i] + "V.png"

        img = cv2.imread(pic, 0)
        img2 = cv2.imread(pic2, 0)
        maxIntensity = 255.0  # depends on dtype of image data
        x = arange(maxIntensity)

        # Parameters for manipulating image data
        phi = 1
        theta = 1

        # Increase intensity such that
        # dark pixels become much brighter,
        # bright pixels become slightly bright
        newImage1 = (maxIntensity / phi) * (img / (maxIntensity / theta))**0.5
        newImage1 = array(newImage1, dtype=uint8)
        newImage1 = cv2.bitwise_not(newImage1)
        newImage2 = (maxIntensity / phi) * (img2 / (maxIntensity / theta))**0.5
        newImage2 = array(newImage2, dtype=uint8)
        newImage2 = cv2.bitwise_not(newImage2)

        cv2.imshow('newImage1', newImage1)
        cv2.imshow('newImage2', newImage2)
        cv2.imwrite((filtered2 + '.png'), newImage1)
        cv2.imwrite((filtered2 + 'V' + '.png'), newImage2)

        print(ftitles[i])
        print(ftitles[i] + "V")

        i += 1
