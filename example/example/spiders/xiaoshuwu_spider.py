# -*- coding: utf-8 -*-
import scrapy


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
        for book in response.css('div.content'):
            # 书名信息在article > h3 > a 元素的title属性里
            # 例如: <a title="A Light in the Attic">A Light in the ...</a>
            name = book.xpath('./h2/a/@title').extract_first()


            # 书价信息在 <p class="price_color">的TEXT中。
            # 例如: <p class="price_color">￡51.77</p>
            jianjie = book.xpath('string(./p[1])').extract_first()
            # jianjie = book.xpath('./p[1]/text()').extract_first()
            yield {
               '书名': name,
               '简介': jianjie,
            }
