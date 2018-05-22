from django.shortcuts import render
from .weatherApi import WeatherApi


def index(request):
    api = WeatherApi('3973fb507ae00b906235026db802504b')
    weather_info = api.search()

    return render(request, 'weather/index.html', {'weather_info': weather_info})
