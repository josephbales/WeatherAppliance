import os, time, yaml
from lib.imagegen import DrawingFacade
from lib.weatherapi import WeatherApi

config_file = open('config.yaml', 'r')
config = yaml.load(config_file, Loader=yaml.FullLoader)

wa_params = {
    'base_api_url': config['weatherApi']['baseUrl'],
    'icon_url': config['weatherApi']['iconUrl'],
    'icon_suffix': config['weatherApi']['iconSuffix'],
    'auth_key': os.environ.get(config['weatherApi']['authEnvVariable'])
}

cc_params = {
    'zipcode': config['weatherApi']['zipCode'],
    'country_code': config['weatherApi']['countryCode']
}

wa = WeatherApi(**wa_params)
print(wa.get_current_conditions(**cc_params))
icon = wa.get_weather_icon('10d')
icon_file = open('/mnt/c/Users/josep/Desktop/icon.png', 'wb')
icon_file.write(icon)
icon_file.close()

df = DrawingFacade(config)
df.draw_sample_svg()

print(time.time())
