# coding:utf-8
import requests
import json
import urllib3
import urllib
import re

sum = 0
# username = "17068619437"
passwd = "aabbcc123"

with open('final.txt') as f:
    for line in f:
        username = line.strip()

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

        # print(result.text)
        res = requests.get("http://www.cezone.cn/m/sign_up/add/8231d6ad85f94b6a8363dba93be73200", headers=headers,
                           cookies=get_result.cookies)

        if re.findall('您已报名', res.text.encode('utf-8')):
            sum += 1
            # pass
        else:
            # print username
            pass

print sum
