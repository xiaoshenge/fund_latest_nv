# -*- coding: utf-8 -*-
import scrapy


class A99fundSpider(scrapy.Spider):
    name = '99fund'
    allowed_domains = ['www.99fund.com']
    start_urls = ['http://www.99fund.com/main/products/jijinhb/index.shtml']

    def parse(self, response):
        body = scrapy.Selector(text=response.body.replace("\t", '').replace("\r","").replace("\n",""))
        fundList = body.xpath('//div[re:test(@id, "con_two_[23456]")]')
        nvList = []
        for i,fund in enumerate(fundList):
            # print fund.extract()
            tr = fund.xpath(".//tr[re:test(@id, '\d{6}')]")
            for i,v in enumerate(tr):
                nvList.append(dict(
                    fundId=v.xpath(".//td[1]/a/text()").extract()[0].strip(),
                    fundName=v.xpath('.//td[2]//a/text()').extract()[0].strip(),
                    netValueDate=v.xpath('.//td[3]/text()').extract()[0].strip(),
                    netValue=v.xpath('.//td[4]/text()').extract()[0].strip(),
                    accumNetValue=v.xpath('.//td[5]/text()').extract()[0].strip(),
                    unitNetChngPct=v.xpath('.//td[6]/span/text()').extract()[0].strip()
                ))

        for i,v in enumerate(nvList):
            print str(v)
