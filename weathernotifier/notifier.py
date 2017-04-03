import notify2
from .location import get_location
from .weather import get_weather


def notify():
    place = get_location()
    resp = get_weather(place)

    # Notification Tool

    notify2.init("Weather Notifier")
    n = notify2.Notification("Weather Details", str(resp))
    n.show()


if __name__ == '__main__':
    notify()