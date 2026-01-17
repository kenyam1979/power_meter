import os
import requests
import json
import datetime


def call_zabbix_api(item_id: str, value: float) -> dict:

  token = os.environ["ZABBIX_API_TOKEN"]
  url = os.environ["ZABBIX_API_URL"]

  # Prepare API header
  headers = {
    "Authorization": token,
    "Content-Type": "application/json-rpc"
    }

  # Prepare data
  unixtime = int(datetime.datetime.now().timestamp())
  nanosec = int(datetime.datetime.now().microsecond * 1000)

  data = {
    "jsonrpc":"2.0",
    "method":"history.push",
    "params":{
      "itemid":item_id,
      "value":value,
      "clock":unixtime,
      "ns":nanosec},
    "id":1
    }

  # Call API
  response = requests.post(url, 
                           headers=headers,
                           data=json.dumps(data))

  # Response
  data = response.json()
  # print(json.dumps(data, indent=2))

  return data


# Test
# ITEM_ID = "69140"
# call_zabbix_api(ITEM_ID, 123.456)
