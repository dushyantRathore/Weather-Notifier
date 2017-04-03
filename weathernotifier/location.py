import googlemaps
import requests
import json


def get_location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']

    gmaps = googlemaps.Client(key='AIzaSyC8Ny7X4cuCOd_9SE21raopnTC-KswEs0Y')
    API_key = "AIzaSyC8Ny7X4cuCOd_9SE21raopnTC-KswEs0Y"

    # Request
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str(lon) + "&key=" + str(API_key)
    x = requests.get(url)
    resp = json.loads(x.text)

    l = len(resp["results"][0]["address_components"])

    # print l

    for i in range(0,l):
        if resp["results"][0]["address_components"][i]["types"][0] == "administrative_area_level_1":
            index = i
            break

    return resp["results"][0]["address_components"][index]["long_name"]




