import pytest

from unittest.mock import Mock
import sys

# Remove cached modules to ensure fresh import
if "power_meter.lib.ct_sensor" in sys.modules:
    del sys.modules["power_meter.lib.ct_sensor"]
if "adafruit_ads1x15" in sys.modules:
    del sys.modules["adafruit_ads1x15"]
if "adafruit_ads1x15.ads1x15" in sys.modules:
    del sys.modules["adafruit_ads1x15.ads1x15"]

# Create mock modules before importing
sys.modules["board"] = Mock()

mock_ads1x15_module = Mock()
mock_ads1x15_module.ads1x15.Pin.A0 = 0
mock_ads1x15_module.ads1x15.Pin.A1 = 1
mock_ads1x15_module.ads1x15.Pin.A2 = 2
mock_ads1x15_module.ads1x15.Pin.A3 = 3
class MockAnalogIn:
    def __init__(self, ads, pin):
        self.ads = ads
        self.pin = pin

mock_ads1x15_module.AnalogIn = MockAnalogIn

sys.modules["adafruit_ads1x15"] = mock_ads1x15_module


def test_read_power():
    class MockResponse:
        voltage = 0.0

    from power_meter.lib.ct_sensor import read_power

    chan = MockResponse()
    chan.voltage = 1.0

    watt = read_power(chan)

    assert watt == 2000.0  # 1.0V -> 20A -> 2000W


def test_get_channel():

    from power_meter.lib.ct_sensor import get_channel

    ads = Mock()
    chan0 = get_channel(ads, 0)
    chan1 = get_channel(ads, 1)
    chan2 = get_channel(ads, 2)
    chan3 = get_channel(ads, 3)

    assert chan0.pin == 0
    assert chan1.pin == 1
    assert chan2.pin == 2
    assert chan3.pin == 3

    with pytest.raises(ValueError):
        get_channel(ads, 4)
