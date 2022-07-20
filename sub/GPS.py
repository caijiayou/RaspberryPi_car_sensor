import pynmea2
import serial
import time
import string


def gps():
    while 1:
        try:
            #get GPS_data
            port = "/dev/ttyAMA0"
            ser = serial.Serial(port,baudrate=9600,timeout=0.5)
            dataout = pynmea2.NMEAStreamReader()
            newdata = ser.readline()

            #cut GPS_data
            if newdata[0:6]== b"$GNRMC":
                # print('\n'*3)
                gps = newdata[newdata.index(b","): newdata.index(b"E")]
                lat = gps[gps.index(b"A")+2: gps.index(b"N")-1]
                lon = gps[gps.index(b"N")+2: len(gps)-1]

                #data bytes to string
                gps = bytes.decode(gps)
                lat = bytes.decode(lat)
                lon = bytes.decode(lon)
                # print('GPS: ', gps)
                # print('latitude: ', lat)
                # print('longitude: ', lon)

                #latitude & longitude unit conversion
                f_lat = lat[2:]
                d_lat = lat[:2]
                d_lat = float(f_lat)/60 + float(d_lat)

                f_lon = lon[3:]
                d_lon = lon[:3]
                d_lon = float(f_lon)/60 + float(d_lon)
                # print('========================================')
                # print('latitude: ', d_lat)
                # print('longitude: ', d_lon)
                # print('========================================')
                return d_lat, d_lon
                break
        except:
            print('Not connected')
            time.sleep(0.3)
            continue

if __name__==('__main__'):
    while True:
        lat, lon = gps()
        print('\n'*5)
        print('========================================')
        print('latitude: ', lat)
        print('longitude: ', lon)
        print('========================================')
        

