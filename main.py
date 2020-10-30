import yaml
from Facades.WeatherFacade import WeatherFacade
from Facades.DrawingFacade import DrawingFacade


file = open('config.yaml', 'r')
config = yaml.load(file, Loader=yaml.FullLoader)

wf = WeatherFacade(config)
conditions = wf.get_current_conditions(config['apiWeatherGov']['weatherStation'])
print(conditions.conditions_desc)

df = DrawingFacade(config)
df.draw_sample_svg()
