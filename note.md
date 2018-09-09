# 学习笔记
- ``settings.py``中设置``pipline``时用``tourism_website.pipelines.MongoDBPipeline`` 格式，开头是当前scrapy项目名称
- ``start_urls``当中不必特意去排除无法访问的地址，在开始抓取报纸的时候，我总想有的报纸周末或者其他特定的日期不发行，所以是不是加一个``try/except``来排除，其实完全想多了，爬虫随时都有可能遇到无法访问的地址，如果这个都在框架中没有解决，而要在最后的脚本中来排雷的话那跟自己造轮子则没有区别。
- scrapy当中的xpath选择器不支持``<tbody>``标签，推测也不支持``<thead>\<tfoot>``等这类上古时代构建网页的标签，参考链接： [stackoverflow](https://stackoverflow.com/questions/18241029/why-does-my-xpath-query-scraping-html-tables-only-work-in-firebug-but-not-the)和[CSDN](https://blog.csdn.net/lishk314/article/details/44916827)。在复制好xpath时，直接删除此类标签即可。
- 修正上一条，``tbody`` 问题产生应该是应为浏览器自动补齐了部分元素造成，可以用进入``scrapy shell``，用fetch(url)访问网页，然后print(response.decode('utf-8'))查看scrapy读取网页的源代码