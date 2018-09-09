import datetime


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

