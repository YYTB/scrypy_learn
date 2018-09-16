import datetime,re


start_date = datetime.date(2010, 7, 28)  # 爬取起始日期,转换为datetime.date日期
finish_date = datetime.date.today()  # 终止爬取日期（默认为当天，即：datetime.date.today()）
days_delta = (finish_date - start_date).days  # 获取天数差，结果为整数
print(days_delta)
urllist = []
for i in range(0, days_delta + 1, 1):
    riqi = finish_date - datetime.timedelta(days=i)
    riqi_s = str(riqi).split('-')
    url = 'http://epaper.newsyc.com/ycrb/html/{}-{}/{}/node_2.htm'.format(riqi_s[0], riqi_s[1], riqi_s[2])
    urllist.append(url)
    print(url)
print(urllist)

searchdate = re.search(r'(\d{4})-(\d{2})/(\d{2})', 'http://epaper.newsyc.com/ycrb/html/2018-09/10/content_691327.htm')
print('{},{},{}'.format(searchdate.group(1),searchdate.group(2),searchdate.group(3)))

print(str(datetime.date.today()).split('-'))
riqi_s = str(datetime.date.today()).split('-')
base_url = "http://epaper.newsyc.com/ycrb/html"
start_urls = ['{}/{}-{}/{}/node_2.htm'.format(base_url, riqi_s[0], riqi_s[1], riqi_s[2])]
print(start_urls)