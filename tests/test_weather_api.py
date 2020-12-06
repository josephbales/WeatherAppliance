import pytest

from src.weather_api import translate_wind_dir

@pytest.mark.parametrize("test_input,expected",
                         [(11, 'N'),
                          (358, 'N'),
                          (346, 'NNW'),
                          (89, 'E')])
def test_wind_dir_should_be(test_input, expected):
    assert translate_wind_dir(test_input) == expected
