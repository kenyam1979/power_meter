import math
import time
import board
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15


# def initialize_sensor() -> AnalogIn:
#     # Create the I2C bus
#     i2c = board.I2C()

#     # Create the ADC object using the I2C bus
#     ads = ADS1115(i2c)

#     # ADC Configuration
#     ads.mode = ads1x15.Mode.CONTINUOUS
#     ads.data_rate = 860

#     # Create single-ended input on channel 0
#     ch = AnalogIn(ads, ads1x15.Pin.A0)
#     # chan = AnalogIn(ads, ads1x15.Pin.A0, ads1x15.Pin.A1)

#     return ch


def initialize_ads1115() -> ADS1115:
    """Initialize and return the ADS1115 object.
    Returns:
        ADS1115: The initialized ADS1115 object.
    Raises:
        RuntimeError: If I2C bus or ADS1115 initialization fails.
    """
    try:
        # Create the I2C bus
        i2c = board.I2C()
        if i2c is None:
            raise RuntimeError("Failed to initialize I2C bus")

        # Create the ADC object using the I2C bus
        ads = ADS1115(i2c)
        if ads is None:
            raise RuntimeError("Failed to initialize ADS1115")

        # ADC Configuration
        ads.mode = ads1x15.Mode.CONTINUOUS
        ads.data_rate = 860

        return ads
    except Exception as e:
        raise RuntimeError(f"Failed to initialize ADS1115: {e}") from e



def get_channel(ads: ADS1115, channel: int) -> AnalogIn:
    """Get the specified channel from the ADS1115 object.
    Args:
        ads (ADS1115): The ADS1115 object.
        channel (int): The channel number (0-3).
    Returns:
        AnalogIn: The specified channel as an AnalogIn object.
    Raises:
        ValueError: If the channel number is invalid.
        RuntimeError: If the channel initialization fails.
    """

    try:
        if channel == 0:
            return AnalogIn(ads, ads1x15.Pin.A0)
        elif channel == 1:
            return AnalogIn(ads, ads1x15.Pin.A1)
        elif channel == 2:
            return AnalogIn(ads, ads1x15.Pin.A2)
        elif channel == 3:
            return AnalogIn(ads, ads1x15.Pin.A3)
        else:
            raise ValueError("Invalid channel number. Must be 0-3.")
    except Exception as e:
        raise RuntimeError(f"Failed to get channel {channel}: {e}") from e



def read_power(chan: AnalogIn) -> float:
    """Read power from the given channel.
    Args:
        chan (AnalogIn): The channel to read from.
    Returns:
        float: The estimated power in Watts.
    Raises:
        RuntimeError: If reading from the channel fails.
    """
    counter = 0
    voltage_ch = 0.0
    sum_ch = 0.0

    # Read sensor voltage for 1 second
    t0 = time.time()
    try:
        while time.time() - t0 < 1:
            voltage_ch = chan.voltage
            sum_ch += voltage_ch**2
            counter += 1

        if counter == 0:
            raise RuntimeError("No readings taken from the channel.")

        # Calculate RMS voltage
        voltage_ch = math.sqrt(sum_ch / counter)

        # Convert in Watt
        current_ch = voltage_ch * 2000.0 / 100.0  # 20A/1V, 100 Ohm burden resistor
        watt_ch = current_ch * 100.0  # Assuming 100V supply voltage

        return watt_ch
    except Exception as e:
        raise RuntimeError(f"Failed to read power from channel: {e}") from e


# Test
# ch = initialize_sensor()
# for t in range(10):
#   print(f"Power: {read_power(ch):.3f}W")
