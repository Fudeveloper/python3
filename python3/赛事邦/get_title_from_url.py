# coding=utf-8
import requests
import re

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)',
}
res = requests.get("http://www.fsdpp.cn/sheji/index_32.html", headers=headers)

pattern = re.compile(r'<h2 class="entry-title"><a href=".*?" target="_blank">(.*?)</a></h2>', re.S)
# print res.content.decode('gb2312')
results = re.findall(pattern, res.content.decode('gb2312'))
# print results

for i in results:
    with open('title.txt','a') as f:
        f.write(i+'\n')
