import requests
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)',

}
res = requests.get("http://www.ivsky.com/",headers=headers)

print res.text