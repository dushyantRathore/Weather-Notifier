import notify2
from location import get_location
from weather import get_weather


def notify():

    icon_path = "/home/dushyant/Desktop/Github/Weather-Notifier/weathernotifier/Weather-icon.png"

    place = get_location()
    resp = get_weather(place)

    # print resp

    result = ''
    result += "Place : " + str(resp[0]["Place"])
    result += "\nStatus : " + str(resp[6])
    result += "\nCurrent Temperature (Celcius) : " + str(resp[1]["temp"])
    result += "\nMax Temperature (Celcius) : " + str(resp[1]["temp_max"])
    result += "\nMin Temperature (Celcius) : " + str(resp[1]["temp_min"])
    result += "\nWind Speed (m/s) : " + str(resp[2]["speed"])
    result += "\nHumidity (%) : " + str(resp[3])
    result += "\nPressure (hpa) : " + str(resp[4]["press"])
    result += "\nCloud Cover (%) : " + str(resp[5])

    # print result

    # Notification Tool

    notify2.init("Weather Notifier")
    n = notify2.Notification("Weather Details", icon=icon_path)
    n.update("Weather Details", result)
    n.show()


if __name__ == '__main__':
    notify()