import requests
import json
import datetime

TOKEN = "Bearer bfa02eeb039926324e80aefdefde96a9b7eac1cb89f8a607326f411a41ed70f5"
URL = "http://ec2-44-222-69-151.compute-1.amazonaws.com/api_jsonrpc.php"

ITEM_ID = "69140"


def call_zabbix_api(item_id: str, value: float) -> dict:

# Prepare API header
  headers = {
    "Authorization": TOKEN,
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
  response = requests.post(URL, 
                           headers=headers,
                           data=json.dumps(data))

  # Response
  data = response.json()
  # print(json.dumps(data, indent=2))

  return data

# Test
# call_zabbix_api(ITEM_ID, 123.456)
