# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TourismWebsiteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class jiangxi_yichunItem(scrapy.Item):
    content = scrapy.Field()  # 文章内容
    title = scrapy.Field()  # 文章标题
    release_time = scrapy.Field()  # 文章发布时间
    crawl_time = scrapy.Field()  # 文章爬取时间
    url = scrapy.Field()  # 文章链接
    column = scrapy.Field()  # 文章所在栏目
