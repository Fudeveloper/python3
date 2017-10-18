import requests
import re
response = requests.get(
    "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%95%86%E4%B8%9A&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E5%95%86%E4%B8%9A&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=800&rn=800",
    verify=False)

re_s = re.compile('"thumbURL":"(.*?)"', re.S)
results = re.findall(re_s, response.content)
# print len(results)
print results
# print response.content

























