# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem
import json
class DouyuImageSpider(scrapy.Spider):
    name = 'douyu_image'
    allowed_domains = ['image.baidu.com']
    offset = 0
    basic_url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%95%86%E4%B8%9A&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E5%95%86%E4%B8%9A&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={0}&rn=30'.format(offset)

    start_urls = [basic_url]

    def parse(self, response):
        # 把json格式的数据转换为python格式，data段是列表
        data = json.loads(response.text)["data"]

        # 遍历json格式数据文本，取出各字段值
        for each in data:
            # 初始化模型对象
            item = DouyuItem()
            # 昵称
            item['nickname'] = each['di']
            # 图片
            item['imagelink'] = each['thumbURL']

            # 将item返回给pipelines处理
            yield item
        # 调用一次parse方法后，处理url
        self.offset += 30
        # 准备发送下一个请求
        yield scrapy.Request(self.basic_url+str(self.offset),callback=self.parse)
