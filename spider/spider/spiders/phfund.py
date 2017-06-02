# -*- coding: utf-8 -*-
import scrapy
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class PhfundSpider(scrapy.Spider):
    name = 'phfund'
    allowed_domains = ['www.phfund.com.cn']
    start_urls = ['http://www.phfund.com.cn/web/fundproducts/getFundList?pageInfo.currentPage=1&pageInfo.pageSize=999']

    def getField(self,item, fieldName):
        if fieldName in item:
            return item[fieldName]
        else:
            return ''

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        for item in jsonresponse['content']['fundList']:
            if item['investmentstyleDesc'] != '货币型':
                tmp = dict(
                    fundId=self.getField(item, 'fundcode'),
                    fundName=self.getField(item, 'fundname'),
                    netValueDate=self.getField(item, 'fdate'),
                    netValue=self.getField(item, 'fundnav'),
                    accumNetValue=self.getField(item, 'addupnav'),
                    unitNetChngPct=self.getField(item, 'upratio'))
