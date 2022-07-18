from sub import *
from sub.DHT11 import dht11
from sub.pm25 import pm25
import os
import time

os.system('clear')
count=0
h, t = dht11(0, 0, 1)
while True:
    try:
        # time.sleep(0.1)
        count += 1
        print(count, end=' | ')
        dustVal = pm25()
        print('dustVal: %f(mg/m3)'%dustVal, end=', ')
        h, t = dht11(h, t, 2)
        print('humidity: %.2f, temperature: %.2f'%(h, t))
    except:
        print('\n=======================')
        continue