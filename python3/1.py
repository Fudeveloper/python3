import requests
import json

headers = {"Content-Type": "application/json"}

jsondata = json.dumps({"head": "GetFresh_AirInfo"})

print(jsondata)
result = requests.post('http://192.168.1.120:80/Handler1.ashx', data=jsondata, headers=headers)

print(result.json())
