# -*- coding: utf-8 -*-
import scrapy
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class HuaanSpider(scrapy.Spider):
    name = 'huaan'
    allowed_domains = ['huaan.com.cn']
    start_urls = ['http://www.huaan.com.cn/fund/supermarket/load.do']

    def getLatestNV(self, list, nvList):
        for item in list:
            nvList.append(dict(
                fundId=item['fundCode'],
                fundName=item['fundName'],
                netValueDate=item['fundDate'],
                netValue=item['fundValue'],
                accumNetValue=item['fundTotalnetValue'],
                unitNetChngPct=item['flucTuateper']))
            if item['fundCode'] == '040035':
                print item


    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())

        nvList = []
        self.getLatestNV(jsonresponse['fundinfoList3'], nvList)
