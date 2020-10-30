class CurrentConditions(object):

    # Need to check for None in all these properties before attempting to format them and soforth
    def __init__(self, data, station_id=None):
        wprops = data['properties']
        self.station_id = station_id
        self.station_url = wprops['station']
        self.timestamp = wprops['timestamp']
        self.metar = wprops['rawMessage'] # METAR format
        self.conditions_desc = wprops['textDescription']
        # data['properties']['presentWeather'] contains METAR codes for conditions under rawString property
        # ex. data['properties']['presentWeather'][0]['rawString']
        # I'm thinking here that I could use this to determine the icon to use based on these codes
        # Perhaps the first code would be the icon, or perhaps I could use multiple
        # Be sure to check for intensity modifiers, ex. -RA (how do we handle VC?)
        # https://en.wikipedia.org/wiki/METAR for codes
        self.tempurature_c = "{:.0f}".format(wprops['temperature']['value']) # In celcius
        self.tempurature_f = "{:.0f}".format((wprops['temperature']['value'] * 9 / 5) + 32) # In celcius
        self.dewpoint_c = "{:.0f}".format(wprops['dewpoint']['value']) # In celcius
        self.dewpoint_f = "{:.0f}".format((wprops['dewpoint']['value'] * 9 / 5) + 32) # In celcius
        self.relative_humidity = "{:.0f}%".format(wprops['relativeHumidity']['value']) # As a percentage ex. 86.42333
        self.barometricPressure = "{:.2f} inches of Hg".format(wprops['barometricPressure']['value'] / 3386) # In Pa
        self.wind_direction = wprops['windDirection']['value'] # It's an angle like 310 or 90 or 45
        # https://www.campbellsci.com/blog/convert-wind-directions
        self.wind_speed = wprops['windSpeed']['value'] # In KPH
        self.wind_gust = wprops['windGust']['value']  # In KPH
        self.visibility = wprops['visibility']['value'] # In meters
