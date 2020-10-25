class CurrentConditions(object):

    def __init__(self, data, station=None):
        self.station = station
        print(data)
        self.tempurature_c = "{:.0f}".format(data['properties']['temperature']['value'])
        self.tempurature_f = "{:.0f}".format((data['properties']['temperature']['value'] * 9/5) + 32)
        self.description = data['properties']['textDescription']
        self.relative_humidity = "{:.0f}%".format(data['properties']['relativeHumidity']['value'])
        self.barometricPressure = "{:.2f} inches of Hg".format(data['properties']['barometricPressure']['value'] / 3386)

