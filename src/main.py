import json, os, time, yaml

from src.models.conditions_and_alerts import conditions_and_alerts_from_dict
from src.image_generator import ImageGenerator
from src.weather_api import WeatherApi

config_file = open('config.yaml', 'r')
config = yaml.load(config_file, Loader=yaml.FullLoader)

wa_params = {
    'base_api_url': config['weatherApi']['baseUrl'],
    'icon_url': config['weatherApi']['iconUrl'],
    'icon_suffix': config['weatherApi']['iconSuffix'],
    'auth_key': os.environ.get(config['weatherApi']['authEnvVariable'])
}

ca_params = {
    'lat': config['locations']['tby']['lat'],
    'lon': config['locations']['tby']['lon']
}

wa = WeatherApi(**wa_params)
# print(wa.get_current_conditions(**cc_params))
# icon = wa.get_weather_icon('10d')
# icon_file = open('/mnt/c/Users/josep/Desktop/icon.png', 'wb')
# icon_file.write(icon)
# icon_file.close()
# cc_json = wa.get_current_conditions(**cc_params)
# print(cc_json)
# cc_result = current_conditions_from_dict(cc_json)

ca_json = wa.get_current_with_alerts(**ca_params)
print(json.dumps(ca_json))
ca_result = conditions_and_alerts_from_dict(ca_json)

df = ImageGenerator(config)
df.draw_sample_svg()

print(time.time())
