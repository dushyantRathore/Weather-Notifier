import pyowm


def get_weather(place):

    owm = pyowm.OWM('a4c44b228e720ea728b757f3aa754c06') # API Key
    observation = owm.weather_at_place(place)

    dic ={}
    dic["Place"] = place

    w = observation.get_weather()

    l=[]
    l.append(dic)
    l.append(w.get_temperature('celsius'))
    l.append(w.get_wind())
    l.append(w.get_humidity())
    l.append(w.get_pressure())

    return l




