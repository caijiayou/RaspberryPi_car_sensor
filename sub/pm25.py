#!/usr/bin/python
# coding=utf-8
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
LED_Pin = 17
GPIO.setup(LED_Pin, GPIO.OUT)
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
# Create single-ended input on channels
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

while True:
    
    os.system('clear')
    print('channel 0| value: %f, voltage: %f'%(chan0.value, chan0.voltage))
    print('channel 1| value: %f, voltage: %f'%(chan1.value, chan1.voltage))
    print('channel 2| value: %f, voltage: %f'%(chan2.value, chan2.voltage))
    print('channel 3| value: %f, voltage: %f'%(chan3.value, chan3.voltage))
    print("---------------------------------------------------")

    GPIO.output(LED_Pin, False)
    time.sleep(0.000280)
    # dustVal=chan0.value
    voltage0 = chan0.voltage
    print('voltage0: ', voltage0)
    dustVal = -1*((0.2-voltage0)/6.5)
    time.sleep(0.000040)
    GPIO.output(LED_Pin, True)
    time.sleep(0.009680)
    print('ans: %f(mg/m3)'%dustVal)
    time.sleep(0.5)