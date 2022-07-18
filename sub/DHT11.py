# #參考網站:https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def dht11(h, t, count):
    '''
        call this function return humidity and temperature.
        dht_pin = 4
    '''
    if count==1:
        for i in range(100):
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            if humidity!=None or temperature!=None:
                nh=humidity
                nt=temperature
                return nh, nt
                break
    
    if count==2:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity==None or temperature==None:
            return h, t
        else:
            return humidity, temperature
            
    

if __name__ == '__main__':
    h, t = dht11(0, 0, 1)
    while True:
        h, t = dht11(h, t, 2)
        print(h, t)