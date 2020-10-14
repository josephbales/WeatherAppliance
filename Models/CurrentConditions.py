class CurrentConditions:

    def __init__(self,
                 station=None,
                 tempurature_f=None,
                 tempurature_c=None,
                 description=None,
                 relative_humidity=None,
                 barometricPressure=None):
        self.station = station
        self.tempurature_f = tempurature_f
        self.tempurature_c = tempurature_c
        self.description = description
        self.relative_humidity = relative_humidity
        self.barometricPressure = barometricPressure