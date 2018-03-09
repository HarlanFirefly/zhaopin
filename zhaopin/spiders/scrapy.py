# coding=utf-8
from scrapy import Request
from scrapy.spiders import Spider
from zhaopin.items import ZhaopinItem


class jobSpider(Spider):
    name = 'jobspider'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER',
        'Accept': 'text/css,*/*;q=0.1',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': 'close'
    }
    start_urls=['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw=python&isadv=0&sg=781ae55b444f452f9fc6aa18eea495e3&p='+str(i) for i in range(1,90)]
    def parse(self, response):
        item = ZhaopinItem()
        jobs = response.xpath('//table[@class="newlist"]')[1:]
        for job in jobs:
            item['jobname'] = job.xpath('.//td[@class="zwmc"]//div/a[1]/text()').extract_first()
            item['companyname'] = job.xpath('.//td[@class="gsmc"]/a[1]/text()').extract_first()
            item['salary'] = job.xpath('.//td[@class="zwyx"]/text()').extract_first()
            item['workingplace'] = job.xpath('.//td[@class="gzdd"]/text()').extract_first()
            item['posttime'] = job.xpath('.//td[@class="gxsj"]/span/text()').extract_first()
            yield item