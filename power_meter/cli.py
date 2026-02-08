import datetime

from .lib.ct_sensor import (
    get_channel,
    initialize_ads1115,
    initialize_sensor,
    read_power,
)
from .lib.zabbix_api import call_zabbix_api, log_dump


def main():
    ITEM_ID = "69140" # Redline

    # Initialize sensor
    # chan = initialize_sensor()
    ads = initialize_ads1115()

    # Read channel 0
    chan = get_channel(ads, 0)
    power_value = read_power(chan)

    # Send data to Zabbix API
    response = call_zabbix_api(ITEM_ID, power_value)

    # Record log
    now = datetime.datetime.now()
    date = now.strftime("%Y%m%d")
    time = now.strftime("%Y%m%d %H%M%S")
    log_file = f"./log/zabbix_api_log_{date}.txt"
    log_dump(response, log_file, time)
