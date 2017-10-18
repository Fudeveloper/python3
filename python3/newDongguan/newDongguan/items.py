# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewdongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # # 编号
    # number = scrapy.Field()
    # # 标题
    # title = scrapy.Field()
    # # 正文
    # content = scrapy.Field()
    # # 地址
    # url = scrapy.Field()

    # 图片链接
    img_link = scrapy.Field()
    # 网页链接
    url_link = scrapy.Field()
    # 图片存储路径
    image_path = scrapy.Field()

