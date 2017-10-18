import requests

headers = {"Content-Type": "application/json"}
import json

# json.dumps()
jsondata = json.dumps({"head": "GetMotoInfo"},ensure_ascii=False)
result = requests.post('http://192.168.17.134:8000/recv_data/', data=jsondata, headers=headers)

print(result.text)
# print
