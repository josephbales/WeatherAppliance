import os
import requests


class WeatherGovService(object):

    def __init__(self, config):
        self._base_url = config['ApiWeatherGov']['baseUrl']
        self._headers = {'Authorization': os.environ.get(config['ApiWeatherGov']['authEnvVariable'])}

    def get_alerts_by_zone(self, zone):
        url = f"/alerts/active/zone/{zone}"
        return self.__get_request__(url)
    
    def get_current_conditions_by_station(self, station):
        url = f"/stations/{station}/observations/latest"
        return self.__get_request__(url)

    def get_icon_by_url(self, url):
        response = requests.get(url, headers=self._headers)
        return response
        
    def __get_request__(self, url, params=None):
        response = requests.get(self._base_url + url, headers=self._headers, params=params)
        return response.json()