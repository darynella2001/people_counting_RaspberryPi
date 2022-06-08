import serial
import time
import service

SEND_SERVER_COUNTER = 10
curr_counter = 0

class GPSModuleWrapper:
    def __init__(self):
        port = "/dev/ttyAMA0"
        self.ser = serial.Serial(port, baundrate=9600,)


    def run(self):
        while True:
            data = self.ser.readline()
            gps_data = self.parseGPS(data)

            if gps_data:
                lat, long = gps_data

                lat, long = self.__to_degrees(lat, long)

            curr_counter += 1

            if curr_counter > SEND_SERVER_COUNTER:
                service.send_gps_data(lat, long)
                curr_counter = 0
                
            time.sleep(1)


    def parseGPS(self, gps_data):
        latitude = None
        longitude = None

        if gps_data and len(gps_data) >=6 and gps_data[0:6] == "$GPGGA":
            location_data = gps_data.split(',')
            latitude = location_data[2]
            longitude = location_data[4]

            if latitude != '' and longitude != '':
                return latitude, longitude

        return latitude, longitude

    #https://github.com/girish946/python-gps/blob/master/gps.py
    #filtering: https://github.com/jakee417/Pi-kalman
    def __to_degrees(self, lats, longs):
        """
        converts the raw values of latitude and longitude from gps module into
        the values required by the google maps to display the exact location.
        """
        #NMEA format for latitude is DDMM.mmmm
        #so parsing values for degree, minutes, seconds form the raw value
        lat_deg = lats[0:2]   
        lat_mins = lats[2:4]  
        lat_secs = round(float(lats[5:])*60/10000, 2)
        
        lat_str = lat_deg +  '['+ lat_mins + '(' + str(lat_secs) + ')'

        #NMEA format for longitude is DDDMM.mmmm
        #so parsing values for degree, minutes, seconds form the raw value
        lon_deg = longs[0:3] 
        lon_mins = longs[3:5]
        lon_secs = round(float(longs[6:])*60/10000, 2)
        
        lon_str = lon_deg +  "["+ lon_mins + "(" + str(lon_secs) + ')'

        return [lat_str, lon_str]






















        # s = gps_data.split(",")

        # if s[7] == '0':
        #     print("No sattelite data available")

        #     return


        # time = s[1][0:2] + ":" + s[1][2:4] + ":" + s[1][4:6]
        # lat = decode(s[2])
        # dirLat = s[3]
        # lon = decode(s[4])
        # dirLon = s[5]
        # alt = s[9] + " m"

        # return lat, lon