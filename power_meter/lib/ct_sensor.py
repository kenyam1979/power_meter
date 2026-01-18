import math
import time
import board
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15


def initialize_sensor() -> AnalogIn:
    # Create the I2C bus
    i2c = board.I2C()

    # Create the ADC object using the I2C bus
    ads = ADS1115(i2c)

    # ADC Configuration
    ads.mode = ads1x15.Mode.CONTINUOUS
    ads.data_rate = 860

    # Create single-ended input on channel 0
    ch = AnalogIn(ads, ads1x15.Pin.A0)
    # chan = AnalogIn(ads, ads1x15.Pin.A0, ads1x15.Pin.A1)

    return ch


def read_power(chan: AnalogIn) -> float:
    counter = 0

    voltage_ch = 0.0
    sum_ch = 0.0

    # Read sensor voltage for 1 second
    t0 = time.time()
    while time.time() - t0 < 1:
        voltage_ch = chan.voltage
        sum_ch = sum_ch + voltage_ch**2
        counter = counter + 1

    # Calculate RMS voltage
    voltage_ch = math.sqrt(sum_ch / counter)

    # Convert in Watt
    current_ch = voltage_ch * 2000.0 / 100.0
    watt_ch = current_ch * 100.0

    # print(f'{t} RMS: {voltage_ch:.3f}V, Estimated current: {current_ch:.3f}A, Estimated power: {watt_ch:.3f}W')
    return watt_ch


# Test
# ch = initialize_sensor()
# for t in range(10):
#   print(f"Power: {read_power(ch):.3f}W")
