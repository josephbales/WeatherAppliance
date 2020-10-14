import requests


class WeatherGovService:

    def __init__(self, base_url, default_headers):
        self.base_url = base_url
        self.default_headers = default_headers

    def get_alerts_by_zone(self, zone):
        url = f"/alerts/active/zone/{zone}"
        return self.__get_request__(url)
    
    def get_current_conditions_by_station(self, station):
        url = f"/stations/{station}/observations/latest"
        return self.__get_request__(url)

    def get_icon_by_url(self, url):
        response = requests.get(url, headers=self.default_headers)
        return response
        
    def __get_request__(self, url, params=None):
        response = requests.get(self.base_url + url, headers=self.default_headers, params=params)
        return response.json()