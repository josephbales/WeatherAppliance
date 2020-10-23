from Services.WeatherGovService import WeatherGovService
from Models.CurrentConditions import CurrentConditions


class WeatherFacade(object):

    def __init__(self, config):
        self._config = config

    def get_current_conditions(self, station):
        wgs = WeatherGovService(config=self._config)
        response = wgs.get_current_conditions_by_station(station)
        return CurrentConditions(response, station)

