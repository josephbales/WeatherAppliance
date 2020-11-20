import json
import logging
import os
import tempfile
import yaml

from src.image_generator import ImageGenerator
from src.models.conditions_and_alerts import conditions_and_alerts_from_dict
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

    ca_json = wa.get_current_with_alerts(**ca_params)
    print(json.dumps(ca_json))
    ca_result = conditions_and_alerts_from_dict(ca_json)

    image_path = wa.get_weather_icon(icon_code=ca_result.current.weather[0].icon)
    print(image_path)

    df = ImageGenerator(config)
    df.draw_sample_svg(image_path)

except Exception as ex:
    logging.exception(ex)
    print('An error occured. Check logs.')

finally:
    logging.debug('Programming is now stopping')

    # from PIL import Image
    #
    # img = Image.open('image.png').convert('LA')
    # img.save('greyscale.png')
