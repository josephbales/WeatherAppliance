import logging
import os
import tempfile
import yaml

from src.image_generator import ImageGenerator
from src.weather_api import WeatherApi

config_file = open('config.yaml', 'r')
config = yaml.load(config_file, Loader=yaml.FullLoader)
logging.basicConfig(filename=config['logFilePath'], format=config['logFormat'], level=config['logLevel'])
logging.debug('Programming is now starting')

try:
    tempDir = tempfile.TemporaryDirectory(prefix=config['tempDirPrefix']);
    config['tempDir'] = tempDir.name

    wa_params = {
        'base_api_url': config['weatherApi']['baseUrl'],
        'icon_url': config['weatherApi']['iconUrl'],
        'icon_suffix': config['weatherApi']['iconSuffix'],
        'auth_key': os.environ.get(config['weatherApi']['authEnvVariable']),
        'temp_dir': config['tempDir']
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

    c_and_a = wa.get_current_with_alerts(**ca_params)
    print(c_and_a.lat)

    black_image_params = {
        'icon_path': '/home/jbales/dev/test_images/wi-day-cloudy.png',
        'temperature': '107',
        'curr_conds': 'Partly Cloudy',
        'feels_like': '88',
        'rel_hum': '45',
        'pressure': '29.92',
        'wind_speed': '5',
        'wind_dir': 'E',
        'sunrise': '07:26:59 CST',
        'sunset': '19:26:59 CST',
        'updated': '2020-11-17 19:26:59 CST',
        'message': "He who laughs last didn't get the joke.",
        'save_path': '/home/jbales/dev/test_images'
    }

    ig = ImageGenerator()
    ig.draw_black_image(**black_image_params)

    red_image_params = {
        # 'message': "Severe Thunderstorm Warning, Tornado Watch, Flash Flood Watch, Winter Weather Advisory",
        'message': "X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O.",
        'save_path': '/home/jbales/dev/test_images'
    }

    ig.draw_red_image(**red_image_params)

except Exception as ex:
    logging.exception(ex)
    print('An error occured. Check logs.')

finally:
    logging.debug('Programming is now stopping')

    # from PIL import Image
    #
    # img = Image.open('image.png').convert('LA')
    # img.save('greyscale.png')
