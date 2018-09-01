# -*- coding: utf-8 -*-
import scrapy,time,re
from ..items import jiangxi_yichunItem

class jiangxi_yichunSpider(scrapy.Spider):
    # 每一个爬虫的唯一标识
    name = "jiangxi_yichun"
    allowed_domains = [
        'yctravel.gov.cn',
    ]
    start_urls = []
    column_dict = {'lykb':'旅游快报','xydt':'行业动态','xjdt':'县级动态'}
    for keys in column_dict.keys():
        start_urls.append('http://www.yctravel.gov.cn/{}/index_1.jhtml'.format(keys))
        # column_name = column_dict[keys]

    def parse(self, response):
        wenzhanglist = response.css('ul.news-list')
        for sel in wenzhanglist.xpath('./li'):
            wenzhang_url = sel.xpath('./h1/a/@href').extract_first()
            yield scrapy.Request(wenzhang_url, callback=self.parse_content)
        # 构造用于匹配下一页链接的正则表达式
        patternre = re.compile(r'index_\d*.jhtml')
        next_url = patternre.search(response.css('span.page-number a[class="Num on"] + a::attr(onclick)').extract_first()).group()
        if next_url:
            # 如果找到下一页的URL，得到绝对路径，构造新的Request 对象
            next_full_url = response.urljoin(next_url)
            yield scrapy.Request(next_full_url, callback=self.parse)


    def parse_content(self, response):
        wenzhang = jiangxi_yichunItem()
        wenzhang['url'] = response.url
        sel = response.css('div.content-area')
        wenzhang['content'] = sel.xpath('string(./div[@class="content"])').extract_first()
        wenzhang['title'] = sel.xpath('string(./div[@class="content_tit"])').extract_first()
        wenzhang['release_time'] = sel.xpath('./div/span[@class="date"]/text()').extract_first()
        wenzhang['crawl_time'] = time.time()
        wenzhang['column'] = response.xpath('//div[@class="dqwz"]/a[3]/text()').extract_first()
        yield wenzhang
