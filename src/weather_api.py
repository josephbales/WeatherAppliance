import os
import requests


def get_request_json(url, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_request_bytes(url, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params, stream=True)
    if response.status_code == 200:
        return response.content
    else:
        return None


class WeatherApi(object):

    def __init__(self, **kwargs):
        self.__base_api_url = kwargs.get('base_api_url')
        self.__icon_url = kwargs.get('icon_url')
        self.__icon_suffix = kwargs.get('icon_suffix')
        self.__auth_key = kwargs.get('auth_key')
        self.__temp_dir = kwargs.get('temp_dir')

    def get_current_conditions(self, **kwargs):
        zipcode = kwargs.get('zipcode')
        country_code = kwargs.get('country_code')
        return self.__get_current_conditions_by_zip_and_country(zipcode, country_code)

    def get_current_with_alerts(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        return self.__get_current_with_alerts(lat, lon)

    def get_weather_icon(self, icon_code):
        url = f'{self.__icon_url}/{icon_code}{self.__icon_suffix}'
        image_bytes = get_request_bytes(url)
        file_path = os.path.join(self.__temp_dir, 'curr_weather_icon.png')
        icon_file = open(file_path, 'wb')
        icon_file.write(image_bytes)
        icon_file.close()
        return icon_file.name

    def __get_current_conditions_by_zip_and_country(self, zipcode, country_code):
        url = f'{self.__base_api_url}/data/2.5/weather'
        params = {'zip': f'{zipcode},{country_code}', 'appid': self.__auth_key}
        return get_request_json(url, params=params)

    def __get_current_with_alerts(self, lat, lon):
        url = f'{self.__base_api_url}/data/2.5/onecall'
        params = {'lat': lat, 'lon': lon, 'exclude': 'minutely,hourly,daily', 'appid': self.__auth_key}
        return get_request_json(url, params=params)
