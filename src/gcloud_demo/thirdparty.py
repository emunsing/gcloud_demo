import os
import attr
import requests
import logging

GMAPS_API_KEY = os.getenv('GOOGLE_API_KEY')
GEOCODING_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

# Function to get latitude and longitude from an address
def get_lat_long(address):
    params = {
        'address': address,
        'key': GMAPS_API_KEY
    }
    response = requests.get(GEOCODING_API_URL, params=params)
    result = response.json()

    if result['status'] == 'OK':
        location = result['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        print(f"Error geocoding {address}: {result['status']}")
        return None, None