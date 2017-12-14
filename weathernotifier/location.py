import googlemaps
import requests
import json
from geopy.geocoders import Nominatim


def get_location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']

    print lat
    print lon

    geolocator = Nominatim()
    location = geolocator.reverse((lat, lon)).address
    location = location.split(",")

    final_loc = location[-4] + "," + location[-3]
    final_loc = final_loc.replace(" ", "")

    return final_loc

#     gmaps = googlemaps.Client(key='AIzaSyA9Nz08jsVYOhOuPG3pYS5YpJ2X4fCuU8U')
#     API_key = "AIzaSyA9Nz08jsVYOhOuPG3pYS5YpJ2X4fCuU8U"
#
#     # Request
#     url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str(lon) + "&key=" + str(API_key)
#     x = requests.get(url)
#     resp = json.loads(x.text)
#
#     # print resp
#
#     l = len(resp["results"][0]["address_components"])
#
#     for i in range(0,l):
#         if resp["results"][0]["address_components"][i]["types"][0] == "administrative_area_level_1":
#             index = i
#             break
#
#     return resp["results"][0]["address_components"][index]["long_name"]
#
#
# x = get_location()
#
# print x

