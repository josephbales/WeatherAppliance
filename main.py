from Facades.WeatherFacade import WeatherFacade

wf = WeatherFacade()
conditions = wf.get_current_conditions('KBNA')
print(conditions.barometricPressure)
