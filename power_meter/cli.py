import datetime

from .lib.ct_sensor import initialize_sensor, read_power
from .lib.zabbix_api import call_zabbix_api, log_dump


def main():
    ITEM_ID = '69140'

    # Initialize sensor
    chan = initialize_sensor()

    # Read power value
    power_value = read_power(chan)

    # Send data to Zabbix API
    response = call_zabbix_api(ITEM_ID, power_value)

    # Record log
    date = datetime.datetime.now().strftime('%Y%m%d')
    log_file = f'./log/zabbix_api_log_{date}.txt'
    log_dump(response, log_file)

