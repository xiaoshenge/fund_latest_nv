# -*- coding: utf-8 -*-
import scrapy
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class EssencefundSpider(scrapy.Spider):
    name = 'essencefund'
    allowed_domains = ['www.essencefund.com']
    start_urls = ['https://www.essencefund.com/servlet/json?funcNo=1000051']

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())

        for v in jsonresponse['DataSet0']:
            if v['fund_type'] != '2' and v['fund_type'] != '99':
                tmp = dict(
                    fundId=v['product_code'],
                    fundName=v['product_name'],
                    netValueDate=v['nav_date'],
                    netValue=v['current_price'],
                    accumNetValue=v['cumulative_net'],
                    unitNetChngPct=v['day_change']
                )
