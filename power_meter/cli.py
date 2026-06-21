# TODO: Consider the proper log strategy and implement  => Log only  at error occurrence
# TODO: Add error handling

import datetime

from .lib.ct_sensor import (
    get_channel,
    initialize_ads1115,
    read_power,
)
from .lib.zabbix_api import call_zabbix_api2, log_dump


def main():

    now = datetime.datetime.now()
 
 
    # Initialize sensor
    # chan = initialize_sensor()
    ads = initialize_ads1115()


    # Read and record channel 0
    chan = get_channel(ads, 0)
    power_value = read_power(chan)
    ITEM_ID0 = "69140"  # Redline
    response0 = call_zabbix_api2(ITEM_ID0, power_value, now)

    # Read and record channel 1
    chan = get_channel(ads, 1)
    power_value = read_power(chan)  
    ITEM_ID1 = "69142"  # Blackline
    response1 = call_zabbix_api2(ITEM_ID1, power_value, now)


    # Record log
    date = now.strftime("%Y%m%d")
    time = now.strftime("%Y%m%d %H%M%S")
    log_file = f"./log/zabbix_api_log_{date}.txt"
    log_dump(response0, log_file, time)
    log_dump(response1, log_file, time)
    