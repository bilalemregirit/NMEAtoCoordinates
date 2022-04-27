import time
import serial
yeni_liste = []
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )

while True:
    port_veri = ser.readline()
    yeni_veri = port_veri.split(", ")
    for x in yeni_veri:    
        
        yepyeni_veri  = x.split(",")
        #print(yepyeni_veri)
        if "$GPGGA" in yepyeni_veri:
            index_g = yepyeni_veri.index("$GPGGA")
            #LATITUDE
            lat = yepyeni_veri[2]
            lat_degree = lat[:2]
            lat_aftz = float(lat[2:10])
            lat_naftz = float(lat_aftz) / 60
            new_lat =  float(lat_degree) +lat_naftz
            #LONGITUDE
            lng = yepyeni_veri[4]
            lng_degree = lng[:3]
            lng_aftz = float(lng[3:10])
            lng_naftz = float(lng_aftz) / 60
            new_lng =  float(lng_degree) +lng_naftz
            
            print(new_lng,new_lat)
    time.sleep(0.1)
    
    
