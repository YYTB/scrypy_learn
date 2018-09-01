# -*- coding: utf-8 -*-
import scrapy
from ..items import xiaoshuwuItem


class BooksSpider(scrapy.Spider):
    # 每一个爬虫的唯一标识
    name = "xiaoshuwu"

    start_urls = []
    for i in range(1,736):
        # 定义爬虫爬取的起始点，起始点可以是多个，这里只有一个
        start_urls.append('http://mebook.cc/page/' + str(i))


    def parse(self, response):
        # 提取数据
        # 每一本书的信息在<article class="product_pod">中，我们使用
        # css()方法找到所有这样的article 元素，并依次迭代
        for sel in response.css('div.content'):
            book = xiaoshuwuItem()

            book['name'] = sel.xpath('./h2/a/@title').extract_first()

            # jianjie = sel.xpath('string(./p[1])').extract_first()
            book['jianjie'] = sel.xpath('./p[1]/text()').extract_first()

            yield book