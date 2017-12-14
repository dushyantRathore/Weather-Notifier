import pyowm
from location import get_location


def get_weather(location):

    # location = get_location()
    #
    # print location

    owm = pyowm.OWM('a4c44b228e720ea728b757f3aa754c06') # API Key
    observation = owm.weather_at_place(location)

    dic ={}
    dic["Place"] = location

    w = observation.get_weather()

    l=[]
    l.append(dic)
    l.append(w.get_temperature('celsius'))
    l.append(w.get_wind())
    l.append(w.get_humidity())
    l.append(w.get_pressure())
    l.append(w.get_clouds())
    l.append(w.get_status())
    l.append(w.get_sunrise_time('iso'))
    l.append(w.get_sunset_time('iso'))

    # print l

    return l

# get_weather()


