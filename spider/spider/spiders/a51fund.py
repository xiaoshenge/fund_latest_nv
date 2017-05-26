# -*- coding: utf-8 -*-
import scrapy


class A51fundSpider(scrapy.Spider):
    name = '51fund'
    allowed_domains = ['www.51fund.com']
    start_urls = ['http://www.51fund.com/images/net_value.xml']

    def parse(self, response):
        fundList = response.xpath('//Fund[not(contains(@Type, "2")) and not(contains(@Type, "Z"))]')
        print fundList
        nvList = []
        for i, v in enumerate(fundList):
            nvList.append(dict(
                fundId=v.xpath('./Fund-Code/text()').extract(),
                fundName=v.xpath('./Fund-Name//text()').extract(),
                netValueDate=v.xpath('./Fund-Date//text()').extract(),
                netValue=v.xpath('./Net-Value//text()').extract(),
                accumNetValue=v.xpath('./Total-Net-Value//text()').extract(),
                unitNetChngPct=v.xpath('./Today-Waver//text()').extract()
            ))
        for i,v in enumerate(nvList):
            print str(v)
