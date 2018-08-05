import reverse_geocoder as rg
import requests
import json


def get_location():
    API_KEY = "7efb02dc0ba8ee84f6f63945578cdcca"
    request_url = "http://api.ipstack.com/check?access_key={}".format(API_KEY)
    r = requests.get(request_url)
    j = json.loads(r.text)
    # print j
    lat = j['latitude']
    lon = j['longitude']

    print lat
    print lon

    results = rg.search((lat,lon))

    return results[0]["name"]


