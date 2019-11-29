import pytesseract
import numpy
import PIL
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

# txt = pytesseract.image_to_string('C:/Users/AJ/Desktop/SS1/2019-07-3109300000.png')
# print(txt)

print(pytesseract.image_to_string(Image.open('2019-07-31093000v.png')))

import subprocess

subprocess.call('C:\Windows\System32\powershell.exe Get-Process', shell=True)
