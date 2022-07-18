from operator import index
import os

from matplotlib.pyplot import title
os.system('cls')

data = "$GPGGA,121253.000,3937.3090,N,11611.6057,E,1,06,1.2,44.6,M,-5.7,M,,0000*72"

t = data[data.index('$'): data.index(',')]
print('title: ', t)

if t=='$GPGGA':
    gps = data[data.index(',')+1: data.index('N')-1]
    
    # longitude and latitude
    longitude = gps[0: gps.index(',')]
    latitude = gps[gps.index(',')+1: len(gps)]

print('gps(longitude and latitude): ', gps)
print('longitude: ', longitude)
print('latitude: ', latitude)