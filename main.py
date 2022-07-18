from sub import *
from sub.DHT11 import dht11
from sub.pm25 import pm25
from sub.compass import compass
import os
import time

start_time = time.time()
os.system('clear')

h, t = dht11(0, 0, 1)
def sampling():
    dustVal = pm25()
    print('dustVal: %f(mg/m3)'%dustVal, end=', ')
    h, t = dht11(h, t, 2)
    print('humidity: %.2f, temperature: %.2f'%(h, t))

while True:
    try:
        
        heading = compass()
        print ("Heading Angle = %d°" %heading)
        
        if start_time/2 == 0:
            sampling()
    
    except:
        print('\n=======================')
        continue