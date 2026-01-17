import math
import time
import board
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15

# Create the I2C bus
i2c = board.I2C()

# Create the ADC object using the I2C bus
ads = ADS1115(i2c)
# you can specify an I2C adress instead of the default 0x48
# ads = ADS.ADS1115(i2c, address=0x49)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ads1x15.Pin.A0)
#chan = AnalogIn(ads, ads1x15.Pin.A0, ads1x15.Pin.A1)

# ADC Configuration
ads.mode = ads1x15.Mode.CONTINUOUS
ads.data_rate = 860

for t in range(50):

    counter= 0
    voltage_ch = 0.0
    sum_ch = 0.0
    t0 = time.time()
    while (time.time() - t0 < 1):      
        voltage_ch = chan.voltage
        sum_ch = sum_ch + voltage_ch**2
        counter = counter + 1
        
    voltage_ch = math.sqrt( sum_ch / counter)

    current_ch = voltage_ch * 2000.0 / 100.0
    watt_ch = current_ch * 100.0

    print(f'{t} RMS: {voltage_ch:.3f}V, Estimated current: {current_ch:.3f}A, Estimated power: {watt_ch:.3f}W')



