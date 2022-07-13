#參考網址:https://www.engineersgarage.com/raspberry-pi-ads1015-ads1115-analog-sensor-interfacing-ir-sensor-interfacing/

import time
import Adafruit_ADS1x15

def adc(GAIN):
    '''
        adc(GAIN), call this function return value
        GAIN增益參數
        2/3  +/- 6.144V
        1    +/- 4.090V
        2    +/- 2.048V
        4    +/- 1.024V
        8    +/- 0.512V
        16   +/- 0.256V
    '''
    adc = Adafruit_ADS1x15.ADS1115()
    value = adc.read_adc(0, gain=GAIN)
    print(value)
    return value

if __name__=='__main__':
    while True:
        try:
            adc(1)
            time.sleep(0.5)
        except:
            print('Error, wait 5sec and continue.')
            time.sleep(5)
            continue