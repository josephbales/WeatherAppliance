import os
import requests


class WeatherGovService(object):

    def __init__(self, base_url, default_headers):
        self._base_url = base_url
        self._headers = default_headers

    def get_alerts_by_zone(self, zone):
        url = f"/alerts/active/zone/{zone}"
        return self.__get_request__(url)
    
    def get_current_conditions_by_station(self, station):
        url = f"/stations/{station}/observations/latest"
        return self.__get_request__(url)

    def get_station_info(self, station):
        url = f"/stations/{station}"
        return self.__get_request__(url)

    def get_icon_by_url(self, url):
        response = requests.get(url, headers=self._headers)
        return response
        
    def __get_request__(self, url, params=None):
        # print(self._base_url + url)
        response = requests.get(self._base_url + url, headers=self._headers, params=params)
        if response.status_code != 200:
            # Do something here if it returns a bad request of some kind, only really care if it's a success
            # If not a success then need to try again later
            # If it fails too many times, need to display an alert on the screen
            # Probably need to just pass back pass or fail out of here and then have a screen controller or something
            # that handles that
            pass

        return response.json()