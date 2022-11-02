# first - Location
# second - Weather
# SORT BY LOCATION NAME

def forecast(*args):
    forecast_data = {}
    sunny_weather = {}
    cloudy_weather = {}
    rainy_weather = {}
    for data in args:
        location = data[0]
        weather = data[1]
        if weather == "Sunny":
            sunny_weather[location] = weather
        elif weather == "Cloudy":
            cloudy_weather[location] = weather
        elif weather == "Rainy":
            rainy_weather[location] = weather

        forecast_data[location] = weather
    result = ""

    sorted_sunny = dict(sorted(sunny_weather.items(), key=lambda x: x[0]))
    sorted_cloudy = dict(sorted(cloudy_weather.items(), key=lambda x: x[0]))
    sorted_rainy = dict(sorted(rainy_weather.items(), key=lambda x: x[0]))
    for key, value in sorted_sunny.items():
        result += f"{key} - {value}\n"
    for key, value in sorted_cloudy.items():
        result += f"{key} - {value}\n"
    for key, value in sorted_rainy.items():
        result += f"{key} - {value}\n"

    return result
