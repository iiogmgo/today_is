import requests
import json
from collections import defaultdict
from datetime import datetime
from .utils import datetime_to_date_str


class WeatherApi:
    CURRENT_API_URL = 'http://api.openweathermap.org/data/2.5/forecast'
    APP_ID = None
    LAT = '37.56826'
    LON = '26.977829'

    def __init__(self, app_id):
        self.APP_ID = app_id

    def add_lat_lon(self, url):
        return url + '&lat=' + self.LAT + '&lon=' + self.LON

    def generate_api_url(self):
        url_with_app_id = self.CURRENT_API_URL + '?APPID=' + self.APP_ID
        return self.add_lat_lon(url_with_app_id)

    def search(self):
        url = self.generate_api_url()

        headers = {}
        response = requests.get(url, headers=headers)
        response_body = json.loads(response.text)

        # 5일간, 3시간씩 데이터 제공
        # 1일당 8개의 데이터 존재
        info_by_day = defaultdict(dict)

        for weather in response_body['list']:
            weather_datetime = datetime.strptime(weather['dt_txt'], '%Y-%m-%d %H:%M:%S')
            weather_date = datetime_to_date_str(weather_datetime)
            if not info_by_day[weather_date]:
                info_by_day[weather_date] = defaultdict(int, max_temp=0, min_temp=1000)

            weather_info = info_by_day[weather_date]

            max_temp = round(weather['main']['temp_max'] - 273.15, 1)
            min_temp = round(weather['main']['temp_min'] - 273.15, 1)

            if weather_info['max_temp'] < max_temp:
                weather_info['max_temp'] = max_temp

            if weather_info['min_temp'] > min_temp:
                weather_info['min_temp'] = min_temp

            info_by_day[weather_date] = dict(info_by_day[weather_date])

        return dict(info_by_day)
