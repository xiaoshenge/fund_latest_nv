# -*- coding: utf-8 -*-
import scrapy
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class JsfundSpider(scrapy.Spider):
    name = 'jsfund'
    allowed_domains = ['www.jsfund.cn']
    start_urls = ['http://www.jsfund.cn/izenportal/service/fundinfo/getFundNAVAll']

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())

        nvList = []
        for item in jsonresponse['data']['result']:
            if item['name'] in ["股票型","指数型","ETF","混合型","债券型","QDII"]:
                for v in item['object']:
                    nvList.append(dict(
                        fundId=v['fundcode'],
                        fundName=v['fundshortname'],
                        netValueDate=v['alternationdate'],
                        netValue=v['nav'],
                        accumNetValue=v['totalnetvalue'],
                        unitNetChngPct=v['sinceyesterday']))
