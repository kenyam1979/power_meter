# TODO: Add error handling

import os
import requests
import json
import datetime


def call_zabbix_api(item_id: str, value: float) -> dict:
    """Call Zabbix API to send data.
    Args:
        item_id (str): The Zabbix item ID.
        value (float): The value to send. 
    Returns:
        dict: The response from the Zabbix API.
    """
    
    # Get environment variables
    token = os.environ["ZABBIX_API_TOKEN"]
    url = os.environ["ZABBIX_API_URL"]

    # Prepare API header
    headers = {"Authorization": token, "Content-Type": "application/json-rpc"}

    # Prepare data
    unixtime = int(datetime.datetime.now().timestamp())
    nanosec = int(datetime.datetime.now().microsecond * 1000)

    data = {
        "jsonrpc": "2.0",
        "method": "history.push",
        "params": {"itemid": item_id, "value": value, "clock": unixtime, "ns": nanosec},
        "id": 1,
    }

    # Call API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response.json()




def log_dump(response: dict, file_path: str, datetime: str) -> None:
    """Dump the API response to a log file.
    Args:
        response (dict): The API response.
        file_path (str): The path to the log file.
        datetime (str): The datetime string for the log entry.
    """ 
    
    with open(file_path, "a") as f:
        f.write(f"{datetime}: {json.dumps(response)}\n")


# Test
# ITEM_ID = "69140"
# call_zabbix_api(ITEM_ID, 123.456)
