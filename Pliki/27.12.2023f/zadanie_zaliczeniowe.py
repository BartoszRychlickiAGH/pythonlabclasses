import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from gpiozero import Button

import time
import random
import csv


def displayInfo(logging, fileNumber, saved = False):
    # clear working buffer of the display
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x, top),       "Status= "+("Logging" if logging else "Standby"),  font=font, fill=255)
    draw.text((x, top+8),     "File=   "+str(fileNumber)+".csv", font=font, fill=255)
    if saved:
        draw.text((x, top+16),    "File saved",  font=font, fill=255)
    draw.text((x, top+25),    "Term.     Start  Stop",  font=font, fill=255)
    # update the display
    disp.image(image)
    disp.display()

# preapre buttons
button = []
button.append(Button(6))
button.append(Button(13))
button.append(Button(19))
button.append(Button(26))

# display initialization
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# clear working buffer of the display
draw.rectangle((0,0,width,height), outline=0, fill=0)

# print some text to working buffer
x = 0
top = -2
draw.text((x, top),       "Podstawy Informatyki",  font=font, fill=255)
draw.text((x, top+8),     "Raspberry Pi W", font=font, fill=255)
draw.text((x, top+16),    "File logger demo",  font=font, fill=255)
draw.text((x, top+25),    "by Piotr Rzeszut 2021",  font=font, fill=255)

# update the display
disp.image(image)
disp.display()
time.sleep(2)


logging = False
fileNumber = 0
data = []

displayInfo(logging, fileNumber)

while True:
    # start logging
    if button[2].is_pressed:
        # do only when was NOT loggine before the button was pressed
        if logging == False:
            logging = True
            fileNumber += 1
            displayInfo(logging, fileNumber)
    # stop logging
    if button[0].is_pressed or button[3].is_pressed:
        if logging == True:
            logging = False
            displayInfo(logging, fileNumber, True)
            with open("log/"+str(fileNumber)+".csv", mode='w') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerows(data)
            data = []
    # terminate
    if button[0].is_pressed:
        break

    if logging == True:
        data.append([time.time(), random.random(), time.time()*2, time.time()**2, random.uniform(10, 20)])
        time.sleep(0.01)

draw.rectangle((0,0,width,height), outline=0, fill=0)
draw.text((x, top),       " File",  font=font, fill=255)
draw.text((x, top+8),     "   Logger", font=font, fill=255)
draw.text((x, top+16),    "      Terminated",  font=font, fill=255)
disp.image(image)
disp.display()