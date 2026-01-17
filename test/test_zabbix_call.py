




#!/usr/bin/env python3

import requests
import json
import datetime



token = "Bearer bfa02eeb039926324e80aefdefde96a9b7eac1cb89f8a607326f411a41ed70f5"
url = "http://ec2-44-222-69-151.compute-1.amazonaws.com/api_jsonrpc.php"

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
        "itemid":"69140",
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

