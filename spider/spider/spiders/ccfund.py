# -*- coding: utf-8 -*-
import scrapy


class CcfundSpider(scrapy.Spider):
    name = 'ccfund'
    allowed_domains = ['http://www.ccfund.com.cn']
    start_urls = ['http://www.ccfund.com.cn/main/index.shtml']

    def parse(self, response):
        body = scrapy.Selector(text=response.body.replace("\t", ""))
        fundList = body.xpath("//ul[@class='funds' and position()>1]")
        for v in fundList.xpath(".//li/table//tr"):
            if len(v.xpath(".//th")) == 8:
                tmp = dict(
                    fundId=v.xpath(".//th[2]/a/text()").extract()[0].strip(),
                    fundName=v.xpath('.//th[2]/text()').extract()[0].strip(),
                    netValueDate=v.xpath('.//th[3]/text()').extract()[0].strip(),
                    netValue=v.xpath('.//th[4]/span/text()').extract()[0].strip(),
                    accumNetValue=v.xpath("concat(.//th[5]/span/text(), .//th[5]/text())").extract()[0].strip(),
                    unitNetChngPct=v.xpath('.//th[6]/span/text()').extract()[0].strip()
                )
                print tmp
