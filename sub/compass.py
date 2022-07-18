import smbus		
from time import sleep  
import math

X_axis_H    = 0x01
Z_axis_H    = 0x05              
Y_axis_H    = 0x03             
declination = -0.00669        
pi          = 3.14159265359

bus = smbus.SMBus(1) 	
Device_Address = 0x0d   

def Magnetometer_Init():
    bus.write_byte_data(Device_Address, 0x0a, 0x81)
    bus.write_byte_data(Device_Address, 0x0b, 0x01)
    bus.write_byte_data(Device_Address, 0x09, 0x11)  
    

def read_raw_data(addr):
    low = bus.read_byte_data(Device_Address, addr-1)
    high = bus.read_byte_data(Device_Address, addr)

    value = ((high << 8) | low)

    if value >= 0x8000:
        value = value - 0x10000
        return value
    else:
        return value

def get_data():
    chipid = bus.read_byte_data(Device_Address, 0x0d)
    Magnetometer_Init() 
    i=0
    heading = None
    [x,y,z] = [None,None,None]
    while i<20:
        status = bus.read_byte_data(Device_Address, 0x06)
        if status == 0x04:
            x = read_raw_data(X_axis_H)
            y = read_raw_data(Y_axis_H)
            z = read_raw_data(Z_axis_H)
            continue
        if status == 0x01:
            x = read_raw_data(X_axis_H)
            y = read_raw_data(Y_axis_H)
            z = read_raw_data(Z_axis_H)
            break
        else:
            sleep(0.01)
            i+=1
            
    if x is None or y is None:
        [x1, y1] = [x, y]
    else:
        c=[[1.0, 0.0, 0.0],
           [0.0, 1.0, 0.0],
           [0.0, 0.0, 1.0]]
        x1 = x * c[0][0] + y * c[0][1] + c[0][2]
        y1 = x * c[1][0] + y * c[1][1] + c[1][2]
    return [x1, y1, z]


def compass():
    [x1, y1, z] = get_data()
    if x1 is None or y1 is None:
        heading = 0
    else:
        heading=math.degrees(math.atan2(y1,x1))

    if(heading < 0):
        heading = heading + 360.0 + math.degrees(declination)
        
    elif(heading > 360.0):
        heading = heading - 360.0

    # print ("Heading Angle = %d°" %heading)
    return heading

if __name__==('__main__'):
    while True:
        compass()