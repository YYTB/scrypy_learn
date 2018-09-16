# -*- coding: utf-8 -*-
import scrapy,time,datetime,re
from ..items import jiangxi_yichunItem
from scrapy.linkextractors import LinkExtractor

class jiangxi_yichunSpider(scrapy.Spider):
    # 每一个爬虫的唯一标识
    name = "jiangxi_yichun_byday"
    allowed_domains = ['newsyc.com']
    riqi_s = str(datetime.date.today()).split('-')
    base_url = "http://epaper.newsyc.com/ycrb/html"
    start_urls = ['{}/{}-{}/{}/node_2.htm'.format(base_url, riqi_s[0], riqi_s[1], riqi_s[2])]

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='/html/body/table/tr[1]/td[1]/table/tr[1]/td/table[3]/tr/td[2]/table')
        links = le.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse_content)
        le = LinkExtractor(restrict_xpaths='/html/body/table/tr[1]/td[2]/table[2]/tr/td[1]/table[3]//td[@class="px12"]')
        next_urls = le.extract_links(response)
        if next_urls:
            for link in next_urls:
                # 如果找到下一页的URL，得到绝对路径，构造新的Request 对象
                yield scrapy.Request(link.url, callback=self.parse)

    def parse_content(self, response):
        wenzhang = jiangxi_yichunItem()
        wenzhang['url'] = response.url
        # 以下提取报道内容没有用extract_first的原因是为了保留段落划分信息，直接提取为列表
        wenzhang['content'] = response.xpath('/html/body/table[1]/tr[1]/td[2]/table[4]/tr[2]//p/text()').extract()
        wenzhang['title'] = response.xpath('string(/html/body/table[1]/tr[1]/td[2]/table[3]/tbody)').extract_first().lstrip().rstrip()
        # 通过正则表达式匹配url里面的日期，用来写入报纸发行日期，即release_time字段
        searchdate = re.search(r'(\d{4})-(\d{2})/(\d{2})', wenzhang['url'])
        wenzhang['release_time'] = '{},{},{}'.format(searchdate.group(1),searchdate.group(2),searchdate.group(3))
        wenzhang['crawl_time'] = time.time()
        wenzhang['column'] = response.xpath('/html/body/table[1]/tr[1]/td[1]/table/tr/td/table[2]/tr/td[1]/div/text()').extract_first().lstrip().rstrip('：')
        yield wenzhang
