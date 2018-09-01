# -*- coding: utf-8 -*-
import scrapy,time,re

from scrapy.selector import Selector

text= """

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="renderer" content="webkit|ie-stand">
	<title>旅游快报 - 宜春旅游政务网</title>
	<meta http-equiv="keywords" content="旅游快报"/>
	<meta http-equiv="description" content="旅游快报"/>
	<meta name="title" content="宜春旅游政务网">
	<meta name="robots" content="index, follow"/>
	<meta name="Baiduspider" content="index, follow"/>
	<link href="/r/cms/www/default/css/base-style.css" rel="stylesheet" type="text/css">
	<link href="/r/cms/www/default/css/common.css" rel="stylesheet" type="text/css">
	<link href="/r/cms/www/default/css/list-nr-style.css" rel="stylesheet" type="text/css">
	<script type="text/javascript" src="/r/cms/www/default/js/jquery.min.js"></script>
	<script type="text/javascript" src="/r/cms/www/default/js/date.js"></script>
	<script type="text/javascript" src="/r/cms/www/default/js/nav.js"></script>
</head>
<body>
<div class="wrapper nr-top-wz">
  <div class="layout nr-top-link">
    <div class="fl"><span>您好!欢迎访问宜春市旅游政务网！</span></div>
    <div class="fr"><a class="top-icon" href="http://www.yctravel.gov.cn/">宜春旅游资讯网</a><a class="top-icon" href="http://www.yctravel.gov.cn/lytk/index.jhtml">宜春旅游图片站</a><a class="top-icon" href="http://www.yctravel.gov.cn/English/index.jhtml">English</a></div>
  </div>
</div>
<!-- end 顶部文字区域 -->
<div class="wrapper nr-top-area">
  <div class="layout nr-top-img">
    <a class="logo" href="javascript:;">宜春市旅游政务网</a>
  </div>
</div>
<!-- end 顶部 logo + title -->
<div class="wrapper nr-nav-bg">
  <div class="layout nr-nav-area">
    <ul>
            <li class=""><a href="/">首页</a></li>
      <li class=""><a href="http://www.yctravel.gov.cn/zmyc/index.jhtml" >醉美宜春</a></li>
      <li class="on"><a href="http://www.yctravel.gov.cn/zxdt/index.jhtml" >资讯动态</a></li>
      <li class=""><a href="http://www.yctravel.gov.cn/xxgk/index.jhtml" >信息公开</a></li>
      <li class=""><a href="http://www.yctravel.gov.cn/bsfw/index.jhtml" >办事服务</a></li>
      <li class=""><a href="http://www.yctravel.gov.cn/lyxc/index.jhtml" >旅游宣传</a></li>
      <li class=""><a href="http://www.yctravel.gov.cn/zsxm/index.jhtml" >招商项目</a></li>
      <li class=""><a href="http://www.yctravel.gov.cn/wxzl/index.jhtml" >文献资料</a></li>
      <li class=""><a href="/zxzx/index.jhtml" >互动参与</a></li>
    </ul>
  </div>
</div>
<div class="wrapper time-weather-bg">
  <div class="layout hidden">
    <div class="nr-time-weather fl">
      <em class="tianqi_date"></em>
      <em class="tianqi_week"></em>
      <em class="tianqi_city"></em>
      <em class="tianqi_img"></em>
      <em class="tianqi_wendu"></em>
      <em class="tianqi_feng"></em>
    </div>
    <div class="nr-search-area fr">
      <form action="/search.jspx" target="_blank" id="searchForm">
        <label class="fl">高级搜索：</label>
        <input class="box fl" name="q" type="text">
        <input class="btn fl" type="submit" value="">
      </form>
    </div>
  
  </div>
</div>
<!-- end 导航  --><div class="layout main-content">
	<div class="side-nav fl">
		<h2>资讯动态</h2>
		<ul>
			<li class=""><a href="http://www.yctravel.gov.cn/tzgg/index.jhtml">通知公告</a></li>
			<li class="on"><a href="http://www.yctravel.gov.cn/lykb/index.jhtml">旅游快报</a></li>
			<li class=""><a href="http://www.yctravel.gov.cn/xjdt/index.jhtml">县级动态</a></li>
			<li class=""><a href="http://www.yctravel.gov.cn/xydt/index.jhtml">行业动态</a></li>
		</ul>
	</div>
	<div class="nr-main fr">
		<div class="dqwz"><em>您当前的位置：</em><a href="/">首页</a> &gt; <a href="http://www.yctravel.gov.cn/zxdt/index.jhtml">资讯动态</a> &gt; <a href="http://www.yctravel.gov.cn/lykb/index.jhtml">旅游快报</a></div>
		<ul class="news-list">
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9010.jhtml">骑游同乐，美景共享！宜丰千人骑游活动完美落幕！</a></h1>
			</li>
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9009.jhtml">厉害了！宜丰电视台采拍的新闻又上央视!</a></h1>
			</li>
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9008.jhtml">靖安县获评首批国家生态文明建设示范市县</a></h1>
			</li>
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9007.jhtml">《铜鼓响起来》候选“十大红色旅游经典歌曲”</a></h1>
			</li>
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9006.jhtml">奉新县千人猕猴桃采摘节持续三天</a></h1>
			</li>
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9005.jhtml">铜鼓汤里温泉度假区国庆中秋假期举办帐篷节</a></h1>
			</li>
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9004.jhtml">院线电影《大山的信念》项目组来奉新考察</a></h1>
			</li>
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9003.jhtml">宜丰入围2017中国候鸟旅居小城榜！</a></h1>
			</li>
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9002.jhtml">铜鼓县成功引进桃花山庄农业园亿元旅游项目</a></h1>
			</li>
			<li>
				<span>2017-09-28</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/9001.jhtml">系列剧《河长故事》在靖安县开机拍摄</a></h1>
			</li>
			<li>
				<span>2017-09-18</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8978.jhtml">丰城市旅发委开展星级饭店复核</a></h1>
			</li>
			<li>
				<span>2017-09-15</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8977.jhtml">朱 虹：禅宗圣地—宜春</a></h1>
			</li>
			<li>
				<span>2017-09-15</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8974.jhtml">助力创建全国文明城市，宜丰旅游系统在行动</a></h1>
			</li>
			<li>
				<span>2017-09-15</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8975.jhtml">明月山召开秀美乡村建设和乡村旅游学习考察成果汇报座谈会 </a></h1>
			</li>
			<li>
				<span>2017-09-15</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8972.jhtml">靖安县旅发委召开全县旅游企业安全生产大检查动员会</a></h1>
			</li>
			<li>
				<span>2017-09-15</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8971.jhtml">靖安三爪仑乡生态好，猕猴频繁进村</a></h1>
			</li>
			<li>
				<span>2017-09-15</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8970.jhtml">万载以节为媒体促进乡村旅游旅游快速发展 </a></h1>
			</li>
			<li>
				<span>2017-09-15</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8969.jhtml">大美生态.山水宜丰——宜丰生态文化艺术作品展</a></h1>
			</li>
			<li>
				<span>2017-09-11</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8968.jhtml">厉害了！万载一特产竟吸引了江西卫视的全程拍摄</a></h1>
			</li>
			<li>
				<span>2017-09-11</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8967.jhtml">宜春新媒体走进铜鼓开展“旅游采风行”活动</a></h1>
			</li>
			<li>
				<span>2017-09-11</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8966.jhtml">铜鼓县举办首届鼓文化旅游节暨鼓舞大赛</a></h1>
			</li>
			<li>
				<span>2017-09-05</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8965.jhtml">全省旅游投融资对接会在南昌顺利召开</a></h1>
			</li>
			<li>
				<span>2017-09-04</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8964.jhtml">市旅发委圆满结束2017宁波国际旅游展参展活动</a></h1>
			</li>
			<li>
				<span>2017-09-04</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8963.jhtml">宜春市政协在铜鼓县开展“纪念秋收起义90周年”爱国主义教育活动 </a></h1>
			</li>
			<li>
				<span>2017-09-04</span>
				<h1><a href="http://www.yctravel.gov.cn/lykb/8962.jhtml">宜春市旅游安全四大专项行动检查组来樟树开展旅游安全专项行动抽查工作</a></h1>
			</li>
		</ul>
<div class="page-area">
  <div class="pages">
    <span class="button-area">共1648条记录 6/66页</span>
<a href="#" class="prev" onclick="location.href='index_5.jhtml'"> &lt;&lt; </a>
    <span class="page-number">
     <a class="Num" href="#" onclick="location.href='index.jhtml'">1</a>
      <i class="Num none">...</i>
     <a class="Num" href="#" onclick="location.href='index_4.jhtml'">4</a>
     <a class="Num" href="#" onclick="location.href='index_5.jhtml'">5</a>
     <a class="Num on" href="#" onclick="location.href='index_6.jhtml'">6</a>
     <a class="Num" href="#" onclick="location.href='index_7.jhtml'">7</a>
     <a class="Num" href="#" onclick="location.href='index_8.jhtml'">8</a>
     <i class="Num none">...</i>
     <a class="Num" href="#" onclick="location.href='index_66.jhtml'">66</a>
    </span>
     <a class="next" href="#" onclick="location.href='index_7.jhtml'"> &gt;&gt; </a>
     <span class="button-area"></span>
      </div>
</div>	</div>
	<div class="clear"></div>
</div>
<div class="wrapper footer">
  <div class="layout copyright">
    <p>服务热线电话 (086)-0795-3270639 [ 网询时间 8:30-11:30 14:30-17:30 ]&emsp;点击这里给我发消息&emsp;旅游监督投诉：电话:0795-3279955&emsp;举报邮箱：master@yctravel.gov.cn</p>
    <p>纪检举报:0795-3279525  举报Email:jwzfgw@163.com</p>
    <div class="bottom-nav"  style="display:none">
      <a href="javascript:;">宜春旅游简介</a>|<a href="javascript:;">旅游预订</a>|<a href="javascript:;">在线咨询服务</a>|<a href="javascript:;">关于我们</a>|<a href="javascript:;">宜春景区推荐</a>|<a href="javascript:;">酒店推荐</a>|<a href="javascript:;">网站地图及导读</a>
    </div>
    <p>主办单位：宜春市旅游发展委员会&emsp;承办单位：宜春市旅游信息服务中心 未均许可 严禁转载或镜像&emsp;联系地址：宜春市宜阳大厦中座B722&emsp;邮政编码:336000&emsp;</p>
    <p> copyright©2017www.yctravel.gov.cn All Rights Reserved &emsp;赣ICP备10004638号 &emsp; 网站标识码:3609000004 &emsp; <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=36090202000071" target="_blank">公安备案号 36090202000071</a></p>
    <div class="rwm">
      <div>
        <img src="/r/cms/www/default/images/app.jpg" width="112" height="112">
        <em>掌上宜春</em>
      </div>
      <div>
        <img src="/r/cms/www/default/images/wx.jpg" width="112" height="112">
        <em>微信二维码</em>
      </div>
      <div>
        <img src="/r/cms/www/default/images/wb.jpg" width="112" height="112">
        <em>新浪微博二维码</em>
      </div>
    </div>
    <script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/15/232/0000/40695809/CA152320000406958090003.js' type='text/javascript'%3E%3C/script%3E"));</script>
	<script id="_jiucuo_" sitecode='3609000004' src='http://pucha.kaipuyun.cn/exposure/jiucuo.js'></script>
	<span id="wzndbg"><a href="/u/cms/www/201801/report_tb_3609000004.pdf" target="_blank"><img src="/r/cms/www/default/images/wzndbg.jpg" width="127" height="90"></a></span>
  </div>
</div></body>
</html>
"""
selector = Selector(text=text)
patternRe = re.compile(r'index_\d*.jhtml')
next_url = selector.css('span.page-number a.Num::attr(onclick)').extract_first()
next_url = patternRe.search(selector.css('span.page-number a[class="Num on"] + a::attr(onclick)').extract_first()).group()
print(next_url)
start_urls = ['http://www.yctravel.gov.cn/lykb/index_1.jhtml']
def parse(self, response):
    if next_url:
        # 如果找到下一页的URL，得到绝对路径，构造新的Request 对象
        next_url = scrapy.Request.urljoin(next_url)
    return next_url

