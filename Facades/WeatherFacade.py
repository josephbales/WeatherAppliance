import os
from Services.WeatherGovService import WeatherGovService
from Models.CurrentConditions import CurrentConditions


class WeatherFacade(object):

    def __init__(self, config):
        print(config['ApiWeatherGov']['authEnvVariable'])
        print(os.environ.get(config['ApiWeatherGov']['authEnvVariable']))
        self._base_url = config['ApiWeatherGov']['baseUrl']
        self._default_headers = {'User-Agent': os.environ.get(config['ApiWeatherGov']['authEnvVariable'])}

    def get_current_conditions(self, station):
        wgs = WeatherGovService(self._base_url, self._default_headers)
        response = wgs.get_current_conditions_by_station(station)
        return CurrentConditions(response, station)

