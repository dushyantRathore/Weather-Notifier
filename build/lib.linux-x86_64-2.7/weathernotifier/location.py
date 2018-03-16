import reverse_geocoder as rg
import requests
import json


def get_location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']

    print lat
    print lon

    results = rg.search((lat,lon))

    print results

    return results[0]["name"]



