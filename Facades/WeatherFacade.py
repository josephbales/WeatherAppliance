from Services.WeatherGovService import WeatherGovService
from Models.CurrentConditions import CurrentConditions


class WeatherFacade():

    def get_current_conditions(self, station):
        base_url = 'https://api.weather.gov'
        headers = {'Authorization': '(josephbales.com, joey@josephbales.com)'}
        wgs = WeatherGovService(base_url=base_url, default_headers=headers)
        response = wgs.get_current_conditions_by_station(station)
        cc = CurrentConditions()
        tempC = response['properties']['temperature']['value']
        relHum = response['properties']['relativeHumidity']['value']
        desc = response['properties']['textDescription']
        bp = response['properties']['barometricPressure']['value']
        cc.tempurature_f = "{:.0f}".format((tempC * 9/5) + 32)
        cc.tempurature_c = "{:.0f}".format(tempC)
        cc.station = station
        cc.relative_humidity = "{:.0f}%".format(relHum)
        cc.description = desc
        cc.barometricPressure = "{:.2f} inches of Hg".format(bp / 3386)
        return cc

