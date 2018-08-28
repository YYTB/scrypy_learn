from scrapy.selector import Selector
import scrapy
import requests

text = requests.get('http://www.yctravel.gov.cn/lykb/index.jhtml')

print(text.text)