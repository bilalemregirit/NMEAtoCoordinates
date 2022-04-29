import time
import serial
yeni_liste = []
except_counter=0
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )


while True:
    
    try:
        port_veri = ser.readline()
    except serial.serialutil.SerialException:
        except_counter+=1
        if except_counter == 5:
           print("Serial Port Tikandi!!!!!") 
           break
        time.sleep(1) 
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
            print(new_lat,new_lng)
            print(InorOut(bizim_ev_alani,new_lat,new_lng))
            
    #time.sleep(0.1)
    
