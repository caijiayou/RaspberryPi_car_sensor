#參考網站:https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def dht11():
    '''
        call this function return humidity and temperature.
        dht_pin = 4
    '''
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity==None or temperature==None:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    print('humidity: %f, temperature: %f'%(humidity, temperature))
    # print(humidity, temperature)
    return humidity, temperature

if __name__ == '__main__':
    while True:
        try:
            dht11()
            time.sleep(0.5)
        except:
            print('Error, wiat 5sec and continue.')
            time.sleep(5)
            continue