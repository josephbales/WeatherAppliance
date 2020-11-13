# Generated using https://app.quicktype.io/
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = conditions_and_alerts_from_dict(json.loads(json_string))


def from_str(x):
    assert isinstance(x, str)
    return x


def from_none(x):
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x):
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x):
    assert isinstance(x, float)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Alert:
    def __init__(self, sender_name, event, start, end, description):
        self.sender_name = sender_name
        self.event = event
        self.start = start
        self.end = end
        self.description = description

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        sender_name = from_union([from_str, from_none], obj.get("sender_name"))
        event = from_union([from_str, from_none], obj.get("event"))
        start = from_union([from_int, from_none], obj.get("start"))
        end = from_union([from_int, from_none], obj.get("end"))
        description = from_union([from_str, from_none], obj.get("description"))
        return Alert(sender_name, event, start, end, description)

    def to_dict(self):
        result = {}
        result["sender_name"] = from_union([from_str, from_none], self.sender_name)
        result["event"] = from_union([from_str, from_none], self.event)
        result["start"] = from_union([from_int, from_none], self.start)
        result["end"] = from_union([from_int, from_none], self.end)
        result["description"] = from_union([from_str, from_none], self.description)
        return result


class Rain:
    def __init__(self, the_1_h):
        self.the_1_h = the_1_h

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        the_1_h = from_union([from_float, from_none], obj.get("1h"))
        return Rain(the_1_h)

    def to_dict(self):
        result = {}
        result["1h"] = from_union([to_float, from_none], self.the_1_h)
        return result


class Weather:
    def __init__(self, id, main, description, icon):
        self.id = id
        self.main = main
        self.description = description
        self.icon = icon

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        main = from_union([from_str, from_none], obj.get("main"))
        description = from_union([from_str, from_none], obj.get("description"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        return Weather(id, main, description, icon)

    def to_dict(self):
        result = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["main"] = from_union([from_str, from_none], self.main)
        result["description"] = from_union([from_str, from_none], self.description)
        result["icon"] = from_union([from_str, from_none], self.icon)
        return result


class Current:
    def __init__(self, dt, sunrise, sunset, temp, feels_like, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, wind_deg, wind_gust, weather, rain):
        self.dt = dt
        self.sunrise = sunrise
        self.sunset = sunset
        self.temp = temp
        self.feels_like = feels_like
        self.pressure = pressure
        self.humidity = humidity
        self.dew_point = dew_point
        self.uvi = uvi
        self.clouds = clouds
        self.visibility = visibility
        self.wind_speed = wind_speed
        self.wind_deg = wind_deg
        self.wind_gust = wind_gust
        self.weather = weather
        self.rain = rain

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        dt = from_union([from_int, from_none], obj.get("dt"))
        sunrise = from_union([from_int, from_none], obj.get("sunrise"))
        sunset = from_union([from_int, from_none], obj.get("sunset"))
        temp = from_union([from_float, from_none], obj.get("temp"))
        feels_like = from_union([from_float, from_none], obj.get("feels_like"))
        pressure = from_union([from_int, from_none], obj.get("pressure"))
        humidity = from_union([from_int, from_none], obj.get("humidity"))
        dew_point = from_union([from_float, from_none], obj.get("dew_point"))
        uvi = from_union([from_float, from_none], obj.get("uvi"))
        clouds = from_union([from_int, from_none], obj.get("clouds"))
        visibility = from_union([from_int, from_none], obj.get("visibility"))
        wind_speed = from_union([from_float, from_none], obj.get("wind_speed"))
        wind_deg = from_union([from_int, from_none], obj.get("wind_deg"))
        wind_gust = from_union([from_float, from_none], obj.get("wind_gust"))
        weather = from_union([lambda x: from_list(Weather.from_dict, x), from_none], obj.get("weather"))
        rain = from_union([Rain.from_dict, from_none], obj.get("rain"))
        return Current(dt, sunrise, sunset, temp, feels_like, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, wind_deg, wind_gust, weather, rain)

    def to_dict(self):
        result = {}
        result["dt"] = from_union([from_int, from_none], self.dt)
        result["sunrise"] = from_union([from_int, from_none], self.sunrise)
        result["sunset"] = from_union([from_int, from_none], self.sunset)
        result["temp"] = from_union([to_float, from_none], self.temp)
        result["feels_like"] = from_union([to_float, from_none], self.feels_like)
        result["pressure"] = from_union([from_int, from_none], self.pressure)
        result["humidity"] = from_union([from_int, from_none], self.humidity)
        result["dew_point"] = from_union([to_float, from_none], self.dew_point)
        result["uvi"] = from_union([to_float, from_none], self.uvi)
        result["clouds"] = from_union([from_int, from_none], self.clouds)
        result["visibility"] = from_union([from_int, from_none], self.visibility)
        result["wind_speed"] = from_union([to_float, from_none], self.wind_speed)
        result["wind_deg"] = from_union([from_int, from_none], self.wind_deg)
        result["wind_gust"] = from_union([to_float, from_none], self.wind_gust)
        result["weather"] = from_union([lambda x: from_list(lambda x: to_class(Weather, x), x), from_none], self.weather)
        result["rain"] = from_union([lambda x: to_class(Rain, x), from_none], self.rain)
        return result


class ConditionsAndAlerts:
    def __init__(self, lat, lon, timezone, timezone_offset, current, alerts):
        self.lat = lat
        self.lon = lon
        self.timezone = timezone
        self.timezone_offset = timezone_offset
        self.current = current
        self.alerts = alerts

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        lat = from_union([from_float, from_none], obj.get("lat"))
        lon = from_union([from_float, from_none], obj.get("lon"))
        timezone = from_union([from_str, from_none], obj.get("timezone"))
        timezone_offset = from_union([from_int, from_none], obj.get("timezone_offset"))
        current = from_union([Current.from_dict, from_none], obj.get("current"))
        alerts = from_union([lambda x: from_list(Alert.from_dict, x), from_none], obj.get("alerts"))
        return ConditionsAndAlerts(lat, lon, timezone, timezone_offset, current, alerts)

    def to_dict(self):
        result = {}
        result["lat"] = from_union([to_float, from_none], self.lat)
        result["lon"] = from_union([to_float, from_none], self.lon)
        result["timezone"] = from_union([from_str, from_none], self.timezone)
        result["timezone_offset"] = from_union([from_int, from_none], self.timezone_offset)
        result["current"] = from_union([lambda x: to_class(Current, x), from_none], self.current)
        result["alerts"] = from_union([lambda x: from_list(lambda x: to_class(Alert, x), x), from_none], self.alerts)
        return result


def conditions_and_alerts_from_dict(s):
    return ConditionsAndAlerts.from_dict(s)


def conditions_and_alerts_to_dict(x):
    return to_class(ConditionsAndAlerts, x)
