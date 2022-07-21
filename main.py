from sub import *
from sub.DHT11 import dht11
from sub.pm25 import pm25
from sub.compass import compass
from sub.GPS import gps
from sub.get_time import get_time
from sub.Python_control_Googlesheet import upload_sheet
from sub.Python_control_Googlesheet import read_sheet
import os
import time

#get start_time and clear termino
start_time = time.time()
os.system('clear')

#get init dht11 data
h, t = dht11(0, 0, 1)
def sampling(h, t):
    #init upload_values
    upload_values = []

    getTime = get_time()
    upload_values.append(getTime)

    lat, lon = gps()
    # print('latitude: %.4f, longitude: %.4f'%(lat, lon))
    upload_values.append(lat)
    upload_values.append(lon)

    dustVal = pm25()
    # print('dustVal: %f(mg/m3)'%dustVal, end=', ')
    upload_values.append(dustVal)

    h, t = dht11(h, t, 2)
    # print('humidity: %.2f, temperature: %.2f'%(h, t))
    upload_values.append(t)
    upload_values.append(h)

    print(upload_values)
    return upload_values

sampling_count = 0
while True:
    # try:
    
    heading = compass()
    print ("Heading Angle = %d°" %heading)
    if int((time.time()-start_time))%2 == 0:
        sampling_count += 1
        if sampling_count >= 50:
            upload_values = sampling(h, t)
            data_count = read_sheet(5, 8)
            upload_sheet(int(data_count), upload_values)
            print('upload okay!')
            sampling_count = 0
    
    # except:
    #     print('\n=======================')
    #     continue