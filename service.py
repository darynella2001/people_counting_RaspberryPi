import requests
import os

SERVER_URL = 'localhost:4000'
BUS_ID = os.getenv('BUS_ID')

def send_gps_data(lat, long):
    requests.post(SERVER_URL + f'/routes/{BUS_ID}', data={
        'curr_position_lat': lat,
        'curr_position_long': long
    })


def send_people_count(count):
    requests.post(SERVER_URL + f'/routes/{BUS_ID}', data={
        'nr_people': count
    })