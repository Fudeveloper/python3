import requests
import json
import urllib3
import urllib

username = "13960942437"
passwd = "wo951127"

get_result = requests.get("http://www.cezone.cn/m/login")
# print get_result.cookies
data = {"userName": username, "passwd": passwd}
encode_data = urllib.urlencode(data)
# print(encode_data)
url = "http://www.cezone.cn/m/login"
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)',
              # 'Cache-Control': 'max-age=0',
              # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              # 'Origin': 'http://www.cezone.cn',
              'Upgrade-Insecure-Requests': '1',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Referer': 'http://www.cezone.cn/m/login',
              'Accept-Encoding': 'gzip, deflate'

}

result = requests.post(url=url, data=encode_data, headers=headers, cookies=get_result.cookies)

print(result.text)
