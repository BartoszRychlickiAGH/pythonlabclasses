import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# import matplotlib as plt
import smbus
import numpy as np

from gpiozero import Button

import time
import random
import csv


class sensors:
    def __init__(self):
        # some MPU6050 Registers and their Address

        self.INT_ENABLE = 0x38
        self.ACCEL_XOUT_H = 0x3B

        self.Device_Address_MPU = 0x68  # MPU6050 device address

        self.bus = smbus.SMBus(1)  # or bus = smbus.SMBus(0) for older version boards

        self.MPU_Init()

    def MPU_Init(self):
        # write to sample rate register
        self.bus.write_byte_data(self.Device_Address_MPU, self.SMPLRT_DIV, 7)

        # Write to power management register
        self.bus.write_byte_data(self.Device_Address_MPU, self.PWR_MGMT_1, 1)

        # Write to Configuration register
        self.bus.write_byte_data(self.Device_Address_MPU, self.CONFIG, 0)

        # Write to Gyro configuration register
        self.bus.write_byte_data(self.Device_Address_MPU, self.GYRO_CONFIG, 24)

        # Write to interrupt enable register
        self.bus.write_byte_data(self.Device_Address_MPU, self.INT_ENABLE, 1)
        # Write registers to enable access to magnetometer
        self.bus.write_byte_data(self.Device_Address_MPU, 0x37, 0x02)
        self.bus.write_byte_data(self.Device_Address_MPU, 0x6A, 0x00)
        self.bus.write_byte_data(self.Device_Address_MPU, 0x6B, 0x00)

    def read_raw_data_MPU(self, addr):
        # Accelero and Gyro value are 16-bit
        high = self.bus.read_byte_data(self.Device_Address_MPU, addr)
        low = self.bus.read_byte_data(self.Device_Address_MPU, addr + 1)

        # concatenate higher and lower value
        value = (high << 8) | low

        # to get signed value from mpu6050
        if value > 32768:
            value = value - 65536
        return value

    def read_acc_raw(self):
        # Read Accelerometer raw value
        x = self.read_raw_data_MPU(self.ACCEL_XOUT_H)

        return {"x": x, "unit": "a.u."}

    def read_acc(self):
        # convert using default gain
        datao = self.read_acc_raw()
        datao["x"] = datao["x"] / 16384.0

        datao["unit"] = "G"
        return datao


sensor = sensors()


# def Graphing(): # napisane 14.01.2024
#   plt.xlabel("time - t[s]")
#  plt.ylabel("Pressure - p[Pa]")
# plt.plot(data1)
# plt.show()
# plt.xlabel("time - t[s]")
# plt.ylabel("Acceleration - a[m/s^2]")
# plt.plot(data2)
# plt.show()


def displayInfo(logging, fileNumber, saved=False):
    # clear working buffer of the display
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text(
        (x, top),
        "Status= " + ("Logging" if logging else "Standby"),
        font=font,
        fill=255,
    )
    draw.text((x, top + 8), "File=   " + str(fileNumber) + ".csv", font=font, fill=255)
    if saved:
        draw.text((x, top + 16), "File saved", font=font, fill=255)
    draw.text((x, top + 25), "Start     Freeze  Stop", font=font, fill=255)
    # update the display
    disp.image(image)
    disp.display()


bus = smbus.SMBus(1)
# MS5611_01BXXX address, 0x77(119)
# 0x1E(30) Reset command
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
# MS5611_01BXXX address, 0x77(118)
# 0x40(64) Pressure conversion(OSR = 256) command
bus.write_byte(0x77, 0x40)
time.sleep(0.5)
# Read digital pressure value
# Read data back from 0x00(0), 3 bytes
# D1 MSB2, D1 MSB1, D1 LSB
value = bus.read_i2c_block_data(0x77, 0x00, 3)
D1 = value[0] * 65536 + value[1] * 256 + value[2]
# MS5611_01BXXX address, 0x76(118)
# 0x50(64) Temperature conversion(OSR = 256) command
bus.write_byte(0x77, 0x50)
time.sleep(0.5)
# Read digital temperature value
# Read data back from 0x00(0), 3 bytes
# D2 MSB2, D2 MSB1, D2 LSB
value = bus.read_i2c_block_data(0x77, 0x00, 3)
D2 = value[0] * 65536 + value[1] * 256 + value[2]
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
pressure = ((((D1 * SENS) / 2097152) - OFF) / 32768.0) / 100.0


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
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# clear working buffer of the display
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# print some text to working buffer
x = 0
top = -2
draw.text((x, top), "Badanie ruchu w pionie", font=font, fill=255)
draw.text((x, top + 8), "Rychlicki", font=font, fill=255)
draw.text((x, top + 16), "Ksiazek", font=font, fill=255)
draw.text((x, top + 25), "oby dzialalo", font=font, fill=255)

# update the display
disp.image(image)
disp.display()
time.sleep(2)


logging = False
fileNumber = 0
data1 = []
# data2 = []

displayInfo(logging, fileNumber)

while True:
    # start logging
    if button[2].is_pressed:
        # do only when was NOT loggine before the button was pressed
        if logging == False:
            logging = True
            fileNumber += 1
            displayInfo(logging, fileNumber)

            draw.text((x, top), "Freezen", font=font, fill=255)
            draw.text((x, top + 8), "program", font=font, fill=255)
            disp.image(image)
            disp.display()

    # stop logging
    if button[0].is_pressed or button[3].is_pressed:
        if logging == True:
            logging = False
            displayInfo(logging, fileNumber, True)
            with open(
                "/home/pi/BartoszRychlicki/log/" + str(fileNumber) + ".csv", mode="w"
            ) as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerows(data1)
            data1 = []
            # data2 = []
    # terminate
    if button[0].is_pressed:
        break

    if logging == True:
        data1.append([time.time(), "%.2f " % pressure, sensor.read_acc()])
        # data2.append([time.time()]) # napisane 14.01.2024
        time.sleep(0.01)

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, top), " File", font=font, fill=255)
draw.text((x, top + 8), "   Logger", font=font, fill=255)
draw.text((x, top + 16), "      Terminated", font=font, fill=255)
disp.image(image)
disp.display()
