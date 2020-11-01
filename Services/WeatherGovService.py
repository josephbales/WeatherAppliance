import os
import requests


class WeatherGovService(object):

    def __init__(self, base_url, default_headers):
        self._base_url = base_url
        self._headers = default_headers

    def get_alerts_by_zone(self, zone):
        url = f"/alerts/active/zone/{zone}"
        return self.__get_request__(self._base_url + url)
    
    def get_current_conditions_by_station(self, station):
        url = f"/stations/{station}/observations/latest"
        return self.__get_request__(self._base_url + url)

    def get_station_info(self, station):
        url = f"/stations/{station}"
        return self.__get_request__(self._base_url + url)

    def get_by_full_url(self, url):
        return self.__get_request__(url)
        
    def __get_request__(self, url, params=None):
        response = requests.get(url, headers=self._headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

