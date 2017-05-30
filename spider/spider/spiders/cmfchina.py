# -*- coding: utf-8 -*-
import scrapy

class CmfchinaSpider(scrapy.Spider):
    name = 'cmfchina'
    allowed_domains = ['www.cmfchina.com']
    start_urls = ['http://www.cmfchina.com/main/index/index.shtml']

    def parse(self, response):
        reqs = []
        fundUrls = response.xpath("//div[@class='bdCont' and position()>2 and not( position()=8)]").\
            xpath(".//tr[position()>1]").\
            xpath(".//td[1]//a/@href").extract()
        for fundUrl in fundUrls:
                reqUrl = 'http://' + self.allowed_domains[0] + fundUrl
                req = scrapy.Request(reqUrl, callback=self.parseDetail)
                reqs.append(req)
        return reqs

    @staticmethod
    def parseDetail(response):
        fundId = response.url.split('/')[4]
        fundName = response.xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/h3/text()").extract()[0]
        tr = response.xpath('//*[@id="navContainer"]//tr[2]')
        tmp = dict(
            fundId=fundId,
            fundName=fundName,
            netValueDate=tr.xpath('.//td[1]/text()').extract()[0].strip(),
            netValue=tr.xpath('.//td[2]/text()').extract()[0].strip(),
            accumNetValue=tr.xpath('.//td[3]/text()').extract()[0].strip(),
            unitNetChngPct=tr.xpath('.//td[4]/text()').extract()[0].strip()
        )
        print tmp
