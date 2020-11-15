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

    def get_current_conditions(self, **kwargs):
        zipcode = kwargs.get('zipcode')
        country_code = kwargs.get('country_code')
        return self.__get_current_conditions_by_zip_and_country(zipcode, country_code)

    def get_current_with_alerts(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        return self.__get_current_with_alerts(lat, lon)

    def get_weather_icon(self, icon_code):
        url = '%s/%s%s' % (self.__icon_url, icon_code, self.__icon_suffix)
        return get_request_bytes(url)

    def __get_current_conditions_by_zip_and_country(self, zipcode, country_code):
        url = '%s/data/2.5/weather' % self.__base_api_url
        params = {'zip': '%s,%s' % (zipcode, country_code), 'appid': self.__auth_key}
        return get_request_json(url, params=params)

    def __get_current_with_alerts(self, lat, lon):
        url = '%s/data/2.5/onecall' % self.__base_api_url
        params = {'lat': lat, 'lon': lon, 'exclude': 'minutely,hourly,daily', 'appid': self.__auth_key}
        return get_request_json(url, params=params)
