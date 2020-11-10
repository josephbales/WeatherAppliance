import os, time, yaml
from lib.imagegen import DrawingFacade
from lib.weatherapi import WeatherApi

file = open('config.yaml', 'r')
config = yaml.load(file, Loader=yaml.FullLoader)

wa = WeatherApi(config['apiOpenWeather']['baseUrl'], os.environ.get(config['apiOpenWeather']['authEnvVariable']))
print(wa.get_current_conditions_by_zip_and_country('37076', 'US'))

df = DrawingFacade(config)
df.draw_sample_svg()

print(time.time())
