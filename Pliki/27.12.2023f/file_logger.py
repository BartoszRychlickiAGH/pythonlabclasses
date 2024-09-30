import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import smbus as bus

from gpiozero import Button

import time
import random
import csv


def displayInfo(logging, fileNumber, saved=False):
    # clear working buffer of the display
    draw.rectangle((0, 0, width, height), outline=0, fill=0)  # inicjalizacja ekranu
    draw.text(
        (x, top),
        "Status= " + ("Logging" if logging else "Standby"),
        font=font,
        fill=255,
    )
    draw.text((x, top + 8), "File=   " + str(fileNumber) + ".csv", font=font, fill=255)
    if saved:
        draw.text((x, top + 16), "File saved", font=font, fill=255)
    draw.text((x, top + 25), "Term.     Start  Stop", font=font, fill=255)
    # update the display
    disp.image(image)
    disp.display()


# preapre buttons
button = []
button.append(Button(6))
button.append(Button(13))
button.append(Button(19))


# display initialization
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# clear working buffer of the display
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# print some text to working buffer
x = 0
top = -2
draw.text((x, top), "Badanie ruchu w pionie", font=font, fill=255)
draw.text((x, top + 8), "Wiktor Książek", font=font, fill=255)
draw.text((x, top + 16), "Bartosz Rychlicki", font=font, fill=255)
draw.text((x, top + 25), "27.12.2023r.", font=font, fill=255)

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
    if button[0].is_pressed:
        # do only when was NOT loggine before the button was pressed
        if logging == False:
            logging = True
            fileNumber += 1
            C1 = bus.read_word_data(0x77, 0xA2)
            bus.write_byte(0x77, 0x1E)
        time.sleep(0.5)
        # Read 12 bytes of calibration data
        # Read pressure sensitivity
        data = bus.read_i2c_block_data(0x77, 0xA2, 2)
        C1 = data[0] * 256 + data[1]
        # Read pressure offset
        data = bus.read_i2c_block_data(0x77, 0xA4, 2)
        C2 = data[0] * 256 + data[1]
        # Read temperature coefficient of pressure sensitivity
        data = bus.read_i2c_block_data(0x77, 0xA6, 2)
        C3 = data[0] * 256 + data[1]
        # Read temperature coefficient of pressure offset
        data = bus.read_i2c_block_data(0x77, 0xA8, 2)
        C4 = data[0] * 256 + data[1]
        # Read reference temperature
        data = bus.read_i2c_block_data(0x77, 0xAA, 2)
        C5 = data[0] * 256 + data[1]
        # Read temperature coefficient of the temperature
        data = bus.read_i2c_block_data(0x77, 0xAC, 2)
        C6 = data[0] * 256 + data[1]

        # Komenda konwersji ciśnienia
        bus.write_byte(0x77, 0x40)
        time.sleep(0.5)

        # Odczyt wartości cyfrowego ciśnienia (D1)
        value = bus.read_i2c_block_data(0x77, 0x00, 3)
        D1 = value[0] * 65536 + value[1] * 256 + value[2]

        # Odczyt wartości cyfrowej temperatury (D2)
        value = bus.read_i2c_block_data(0x77, 0x00, 3)
        D2 = value[0] * 65536 + value[1] * 256 + value[2]

        # korekta danych
        dT = D2 - C5 * 256
        TEMP = 2000 + dT * C6 / 8388608
        OFF = C2 * 65536 + (C4 * dT) / 128
        SENS = C1 * 32768 + (C3 * dT) / 256
        T2 = 0
        OFF2 = 0
        SENS2 = 0

        if TEMP >= 2000:
            T2 = 0
            OFF2 = 0
            SENS2 = 0
        elif TEMP < 2000:
            T2 = (dT * dT) / 2147483648
            OFF2 = 5 * ((TEMP - 2000) * (TEMP - 2000)) / 2
            SENS2 = 5 * ((TEMP - 2000) * (TEMP - 2000)) / 4
            if TEMP < -1500:
                OFF2 = OFF2 + 7 * ((TEMP + 1500) * (TEMP + 1500))
                SENS2 = SENS2 + 11 * ((TEMP + 1500) * (TEMP + 1500)) / 2

        TEMP = TEMP - T2
        OFF = OFF - OFF2
        SENS = SENS - SENS2

        # Obliczenie wartości ciśnienia
        pressure = ((((D1 * SENS) / 2097152) - OFF) / 32768.0) / 100.0
        data = pressure
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top), "Pressure= " + str(pressure), font=font, fill=255)
        draw.text((x, top + 8), "Acceleration = " + str(), font=font, fill=255)
        # displayInfo(logging, fileNumber)
    # stop logging
    if button[1].is_pressed or button[2].is_pressed:
        if logging == True:
            logging = False
            displayInfo(logging, fileNumber, True)
            with open("log/" + str(fileNumber) + ".csv", mode="w") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerows(data)
            data = []
    # terminate
    if button[2].is_pressed:
        break

    if logging == True:
        data.append(
            [
                time.time(),
                random.random(),
                time.time() * 2,
                time.time() ** 2,
                random.uniform(10, 20),
            ]
        )
        time.sleep(0.01)

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, top), " File", font=font, fill=255)
draw.text((x, top + 8), "   Logger", font=font, fill=255)
draw.text((x, top + 16), "      Terminated", font=font, fill=255)
disp.image(image)
disp.display()
