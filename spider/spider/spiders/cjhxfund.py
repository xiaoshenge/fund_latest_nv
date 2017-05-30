# -*- coding: utf-8 -*-
import scrapy
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib


class CjhxfundSpider(scrapy.Spider):
    name = 'cjhxfund'
    allowed_domains = ['www.cjhxfund.com']
    start_urls = ['http://www.cjhxfund.com/main/qxcp/index.html']

    def parse(self, response):
        # position not work!!
        # fundList = response.xpath('//div[@class="two" and not(position()=3)]')

        reqs=[]
        fundList = response.xpath('//div[@class="two"]')
        for k,v in enumerate(fundList):
            if k == 4:
                continue
            for fund in v.xpath('.//a'):
                fundId = fund.xpath('./@id').extract()[0]
                fundName = fund.xpath('./text()').extract()[0]
                body = {"funcNo": "906004", "fundid": fundId, "curpage": "1", "numPerPage": "1"}
                req = scrapy.FormRequest('http://www.cjhxfund.com/servlet/json',
                                         formdata=body,
                                     callback=self.parseDetail, meta=dict(fundId=fundId, fundName=fundName))

                reqs.append(req)
        return reqs

    def parseDetail(self,response):
        jsonresponse = json.loads(response.body_as_unicode())
        if len(jsonresponse['results'][0]['data']) == 1:
            tmp = dict(
                fundId=response.meta['fundId'],
                fundName=response.meta['fundName'],
                netValueDate=jsonresponse['results'][0]['data'][0]['settledate'],
                netValue=jsonresponse['results'][0]['data'][0]['nav'],
                accumNetValue=jsonresponse['results'][0]['data'][0]['sumofnav'],
                unitNetChngPct=jsonresponse['results'][0]['data'][0]['shortDaygrouwnth']
            )
            print tmp