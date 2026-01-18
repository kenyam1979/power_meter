#!/usr/bin/env python3
import os
import requests
import json
import datetime


token = os.environ["ZABBIX_API_TOKEN"]
url = os.environ["ZABBIX_API_URL"]

unixtime = int(datetime.datetime.now().timestamp())
nanosec = int(datetime.datetime.now().microsecond * 1000)


#APIheader作成
headers = {
    "Authorization": token,
    "Content-Type": "application/json-rpc"
    }

#Data作成
data = {
    "jsonrpc":"2.0",
    "method":"history.push",
    "params":{
        "itemid":"69141",
        "value":125,
        "clock":unixtime,
        "ns":nanosec},
    "id":1
    }

#requests処理
response = requests.post(url,headers=headers,data=json.dumps(data))

# レスポンス処理とデータ型変更
data = response.json()

# JSONデータを文字列に変換してprintで出力
print(json.dumps(data, indent=2))

