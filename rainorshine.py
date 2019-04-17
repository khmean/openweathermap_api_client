"""
Program: rainorshine.py
Author: Khann Mean
This program will use openweathermap.org API and obtain the current temperature, win
"""

import requests

API_KEY = "391ca8dca14d4a785f9d52917910b3fe"
WS_URL = "https://api.openweathermap.org/data/2.5/weather"
UV_URL = "https://api.openweathermap.org/data/2.5/uvi"


def fetch_weather(s):
    """
    Lookup a US city and report the current weather conditions such as temperature, wind speed
    and UV index.

    Parameters:
    fetch_weather (String): A string of a city typed in by user.

    Returns:
    None.
    """

    # request parameter(s): Start with '?'
    # separate name and value with '='
    # multiple parameter name value pairs are separate with '&'
    # encode space ' ' with '%20'
    request_url = WS_URL + "?q={},US&units=imperial&APIKEY={}".format(s.replace(' ', '%20'), API_KEY)
    # process the url and test to make sure it is connected to the internet
    current_temperature = requests.get(request_url)
    # only with a successful connection with code 200 process the weather information
    if current_temperature.status_code == 200:
        d = current_temperature.json()
        print("Request URL:", request_url)

        # generate the url to get the uv index information from openweather
        uv_index_url = UV_URL + "?lat={}&lon={}&APIKEY={}".format(d["coord"]["lat"], d["coord"]["lon"], API_KEY)
        current_uv_index = requests.get(uv_index_url)
        # store the uv index information into a dictionary
        uv_dict = current_uv_index.json()
        direction_in_degrees = d["wind"]["deg"]

        # determine the wind direction by the given degree
        if direction_in_degrees >= 20 and direction_in_degrees <= 39:
            direction = "N/NE"
        elif direction_in_degrees >= 40 and direction_in_degrees <= 59:
            direction = "NE"
        elif direction_in_degrees >= 60 and direction_in_degrees <= 79:
            direction = "E/NE"
        elif direction_in_degrees >= 80 and direction_in_degrees <= 109:
            direction = "E"
        elif direction_in_degrees >= 110 and direction_in_degrees <= 129:
            direction = "E/SE"
        elif direction_in_degrees >= 130 and direction_in_degrees <= 149:
            direction = "SE"
        elif direction_in_degrees >= 150 and direction_in_degrees <= 169:
            direction = "S/SE"
        elif direction_in_degrees >= 170 and direction_in_degrees <= 199:
            direction = "S"
        elif direction_in_degrees >= 200 and direction_in_degrees <= 219:
            direction = "S/SW"
        elif direction_in_degrees >= 220 and direction_in_degrees <= 239:
            direction = "SW"
        elif direction_in_degrees >= 240 and direction_in_degrees <= 259:
            direction = "W/SW"
        elif direction_in_degrees >= 260 and direction_in_degrees <= 289:
            direction = "W"
        elif direction_in_degrees >= 290 and direction_in_degrees <= 309:
            direction = "W/NW"
        elif direction_in_degrees >= 310 and direction_in_degrees <= 329:
            direction = "NW"
        elif direction_in_degrees >= 330 and direction_in_degrees <= 349:
            direction = "N/NW"
        elif direction_in_degrees >= 350 and direction_in_degrees <= 360:
            direction = "N"
        else:
            direction = "N"  # when the degrees is 1 to 19 set direction to N

        # report the weather information in imperial units such as Fahrenheit
        print("The current temperature in {} is {}".format(s, d["main"]["temp"]) + chr(176) + "F")
        print("The current wind speed is {} at {} MPH".format(direction, d["wind"]["speed"]))
        print("The current UV index is {}".format(uv_dict["value"]))
    else:
        # give an error if it is not a city that can be processed
        print("Hmm I don't think that's a US city please try again...")


if __name__ == "__main__":
    # ask the user for a city to lookup the weather
    s = input("What US City do you need the current weather condition: ")
    fetch_weather(s)